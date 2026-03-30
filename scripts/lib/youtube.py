"""
YouTube data extraction via yt-dlp (free, open source)

Extracts:
- Channel info
- Recent video metadata
- Video transcripts/captions

Requires: yt-dlp installed (pip install yt-dlp)
"""

import subprocess
import json
import sys
import os
from typing import Optional


# Common locations for yt-dlp
YTDLP_PATHS = [
    "yt-dlp",  # In PATH
    os.path.expanduser("~/.local/bin/yt-dlp"),  # Linux user install
    os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp"),  # macOS Python 3.9
    os.path.expanduser("~/Library/Python/3.10/bin/yt-dlp"),  # macOS Python 3.10
    os.path.expanduser("~/Library/Python/3.11/bin/yt-dlp"),  # macOS Python 3.11
    os.path.expanduser("~/Library/Python/3.12/bin/yt-dlp"),  # macOS Python 3.12
    "/usr/local/bin/yt-dlp",  # Homebrew
    "/opt/homebrew/bin/yt-dlp",  # Homebrew on Apple Silicon
]


def find_ytdlp() -> Optional[str]:
    """Find yt-dlp executable."""
    # First try common paths
    for path in YTDLP_PATHS:
        try:
            result = subprocess.run(
                [path, "--version"],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                return path
        except (subprocess.SubprocessError, FileNotFoundError, PermissionError):
            continue

    # Try using python -m yt_dlp
    try:
        result = subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--version"],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"{sys.executable} -m yt_dlp"
    except subprocess.SubprocessError:
        pass

    return None


def run_ytdlp(args: list, timeout: int = 30) -> subprocess.CompletedProcess:
    """Run yt-dlp with the found executable."""
    ytdlp_path = find_ytdlp()
    if not ytdlp_path:
        raise FileNotFoundError("yt-dlp not found")

    # Handle python -m yt_dlp case
    if ytdlp_path.endswith("yt_dlp"):
        cmd = ytdlp_path.split() + args
    else:
        cmd = [ytdlp_path] + args

    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout
    )


def check_ytdlp_installed() -> bool:
    """Check if yt-dlp is installed."""
    return find_ytdlp() is not None


def search_youtube_channel(query: str) -> Optional[dict]:
    """
    Search YouTube for a channel matching the query.

    Args:
        query: Company or person name

    Returns:
        dict with channel URL and basic info
    """
    if not check_ytdlp_installed():
        return {"error": "yt-dlp not found"}

    try:
        # Search for official channel - add "official" to improve accuracy
        result = run_ytdlp(
            [
                "--dump-json",
                "--flat-playlist",
                "--playlist-items", "1",
                f"ytsearch1:{query} official channel"
            ],
            timeout=30
        )

        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout.strip())
            return {
                "channel_url": data.get("channel_url"),
                "channel_id": data.get("channel_id"),
                "uploader": data.get("uploader"),
                "uploader_id": data.get("uploader_id")
            }
    except (subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError):
        pass

    return None


def get_channel_videos(channel_url: str, max_videos: int = 10) -> list:
    """
    Get recent videos from a YouTube channel.

    Args:
        channel_url: YouTube channel URL
        max_videos: Maximum number of videos to fetch

    Returns:
        list of video metadata dicts
    """
    if not check_ytdlp_installed():
        return []

    try:
        result = run_ytdlp(
            [
                "--dump-json",
                "--flat-playlist",
                "--playlist-items", f"1-{max_videos}",
                f"{channel_url}/videos"
            ],
            timeout=60
        )

        videos = []
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line:
                    try:
                        video = json.loads(line)
                        videos.append({
                            "id": video.get("id"),
                            "title": video.get("title"),
                            "url": video.get("url") or f"https://youtube.com/watch?v={video.get('id')}",
                            "duration": video.get("duration"),
                            "view_count": video.get("view_count"),
                            "upload_date": video.get("upload_date")
                        })
                    except json.JSONDecodeError:
                        continue
        return videos

    except (subprocess.SubprocessError, FileNotFoundError):
        return []


def get_video_transcript(video_url: str, max_chars: int = 2000) -> Optional[dict]:
    """
    Extract transcript/captions info from a YouTube video.

    Args:
        video_url: YouTube video URL
        max_chars: Maximum characters to return

    Returns:
        Transcript info dict or None
    """
    if not check_ytdlp_installed():
        return None

    try:
        result = run_ytdlp(
            [
                "--dump-json",
                video_url
            ],
            timeout=30
        )

        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout.strip())

            description = data.get("description", "")
            subtitles = data.get("subtitles", {})
            auto_captions = data.get("automatic_captions", {})

            return {
                "has_subtitles": bool(subtitles),
                "has_auto_captions": bool(auto_captions),
                "description": description[:max_chars] if description else None,
                "available_languages": list(subtitles.keys()) + list(auto_captions.keys())
            }

    except (subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError):
        pass

    return None


def get_youtube_data(query: str) -> dict:
    """
    Main function to get all YouTube data for a target.

    Args:
        query: Company or person name

    Returns:
        dict with channel info, videos, and transcripts
    """
    results = {
        "query": query,
        "channel": None,
        "videos": [],
        "transcript_samples": [],
        "stats": {
            "total_videos_checked": 0,
            "total_views": 0,
            "avg_views": 0
        }
    }

    ytdlp_path = find_ytdlp()
    if not ytdlp_path:
        results["error"] = "yt-dlp not found. Install with: pip install yt-dlp"
        results["note"] = "If installed, add to PATH or check ~/Library/Python/*/bin/"
        return results

    # Search for channel
    channel = search_youtube_channel(query)
    if channel and not channel.get("error") and channel.get("channel_url"):
        results["channel"] = channel

        # Get recent videos
        videos = get_channel_videos(channel["channel_url"], max_videos=10)
        results["videos"] = videos
        results["stats"]["total_videos_checked"] = len(videos)

        # Calculate view stats
        view_counts = [v.get("view_count", 0) for v in videos if v.get("view_count")]
        if view_counts:
            results["stats"]["total_views"] = sum(view_counts)
            results["stats"]["avg_views"] = sum(view_counts) // len(view_counts)

        # Get transcript info for top 3 videos
        for video in videos[:3]:
            if video.get("url"):
                transcript_info = get_video_transcript(video["url"])
                if transcript_info:
                    results["transcript_samples"].append({
                        "video_title": video.get("title"),
                        "video_url": video.get("url"),
                        **transcript_info
                    })

    return results
