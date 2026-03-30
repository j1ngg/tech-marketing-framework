"""
ScrapeCreators API integration (optional, paid)

Provides reliable social media data for Twitter, TikTok, Instagram, Reddit.
Cost: $10 for 5,000 credits

Set SCRAPECREATORS_API_KEY in environment to enable.
Docs: https://scrapecreators.com/docs
"""

import os
import requests
from typing import Optional


API_BASE = "https://api.scrapecreators.com/v1"


def get_api_key() -> Optional[str]:
    """Get API key from environment."""
    return os.environ.get("SCRAPECREATORS_API_KEY")


def is_available() -> bool:
    """Check if ScrapeCreators API is configured."""
    return get_api_key() is not None


def get_twitter_profile(username: str) -> Optional[dict]:
    """
    Get Twitter/X profile data.

    Args:
        username: Twitter username (with or without @)

    Returns:
        dict with profile data or None if unavailable
    """
    api_key = get_api_key()
    if not api_key:
        return None

    clean_username = username.lstrip("@")
    url = f"{API_BASE}/twitter/user/{clean_username}"

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "platform": "twitter",
                "username": clean_username,
                "followers": data.get("followers_count"),
                "following": data.get("following_count"),
                "tweets": data.get("tweet_count"),
                "verified": data.get("verified"),
                "description": data.get("description"),
                "created_at": data.get("created_at"),
                "source": "scrapecreators"
            }
    except requests.RequestException:
        pass

    return None


def get_twitter_tweets(username: str, limit: int = 20) -> Optional[dict]:
    """
    Get recent tweets from a user.

    Args:
        username: Twitter username
        limit: Max tweets to return

    Returns:
        dict with tweets or None
    """
    api_key = get_api_key()
    if not api_key:
        return None

    clean_username = username.lstrip("@")
    url = f"{API_BASE}/twitter/user/{clean_username}/tweets"

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            params={"limit": limit},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            tweets = []
            for tweet in data.get("tweets", [])[:limit]:
                tweets.append({
                    "text": tweet.get("text"),
                    "likes": tweet.get("like_count"),
                    "retweets": tweet.get("retweet_count"),
                    "replies": tweet.get("reply_count"),
                    "created_at": tweet.get("created_at"),
                    "url": tweet.get("url")
                })
            return {
                "username": clean_username,
                "tweets": tweets,
                "source": "scrapecreators"
            }
    except requests.RequestException:
        pass

    return None


def get_tiktok_profile(username: str) -> Optional[dict]:
    """
    Get TikTok profile data.

    Args:
        username: TikTok username

    Returns:
        dict with profile data or None
    """
    api_key = get_api_key()
    if not api_key:
        return None

    clean_username = username.lstrip("@")
    url = f"{API_BASE}/tiktok/user/{clean_username}"

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "platform": "tiktok",
                "username": clean_username,
                "followers": data.get("follower_count"),
                "following": data.get("following_count"),
                "likes": data.get("heart_count"),
                "videos": data.get("video_count"),
                "verified": data.get("verified"),
                "description": data.get("signature"),
                "source": "scrapecreators"
            }
    except requests.RequestException:
        pass

    return None


def get_instagram_profile(username: str) -> Optional[dict]:
    """
    Get Instagram profile data.

    Args:
        username: Instagram username

    Returns:
        dict with profile data or None
    """
    api_key = get_api_key()
    if not api_key:
        return None

    clean_username = username.lstrip("@")
    url = f"{API_BASE}/instagram/user/{clean_username}"

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "platform": "instagram",
                "username": clean_username,
                "followers": data.get("follower_count"),
                "following": data.get("following_count"),
                "posts": data.get("media_count"),
                "verified": data.get("is_verified"),
                "description": data.get("biography"),
                "source": "scrapecreators"
            }
    except requests.RequestException:
        pass

    return None


def get_social_stats(username: str) -> dict:
    """
    Get social media stats across platforms.

    Args:
        username: Username to search

    Returns:
        dict with stats from available platforms
    """
    if not is_available():
        return {
            "available": False,
            "error": "SCRAPECREATORS_API_KEY not set. Get one at scrapecreators.com ($10/5000 credits)",
            "platforms": {}
        }

    results = {
        "available": True,
        "platforms": {}
    }

    twitter = get_twitter_profile(username)
    if twitter:
        results["platforms"]["twitter"] = twitter

    tiktok = get_tiktok_profile(username)
    if tiktok:
        results["platforms"]["tiktok"] = tiktok

    instagram = get_instagram_profile(username)
    if instagram:
        results["platforms"]["instagram"] = instagram

    return results
