#!/usr/bin/env python3
"""
how-they-market research collection script

Collects marketing presence data from free sources:
- Hacker News (Algolia API)
- Reddit (public JSON API)
- YouTube (yt-dlp)
- Social media metrics (ScrapeCreators, optional)

Web search is handled by the Claude agent's built-in WebSearch tool.

Usage:
    python research.py "company name or handle"
    python research.py "@username"

Output:
    JSON to stdout with structured data for agent analysis
"""

import sys
import json
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

from lib.hackernews import search_hackernews
from lib.reddit import search_reddit
from lib.youtube import get_youtube_data
from lib import scrapecreators


def research_target(target: str, focus: str = None) -> dict:
    """
    Research a target across all available sources.

    Args:
        target: Company name, Twitter handle, or URL
        focus: Optional focus area (e.g., "twitter", "youtube", "launches")

    Returns:
        dict with structured research data
    """
    results = {
        "target": target,
        "focus": focus or "full",
        "research_date": datetime.now().isoformat(),
        "sources": {}
    }

    # Normalize target for different searches
    clean_target = target.lstrip("@").strip()

    # Run searches in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {}

        # Hacker News search (free, reliable)
        futures[executor.submit(search_hackernews, clean_target)] = "hackernews"

        # Reddit search (free, reliable)
        futures[executor.submit(search_reddit, clean_target)] = "reddit"

        # YouTube search and transcript extraction (free, requires yt-dlp)
        futures[executor.submit(get_youtube_data, clean_target)] = "youtube"

        # ScrapeCreators for social stats (optional, paid)
        futures[executor.submit(scrapecreators.get_social_stats, clean_target)] = "social_stats"

        # Collect results
        for future in as_completed(futures):
            source_name = futures[future]
            try:
                data = future.result()
                if data:
                    results["sources"][source_name] = data
            except Exception as e:
                results["sources"][source_name] = {"error": str(e)}

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Research how a target markets themselves"
    )
    parser.add_argument(
        "target",
        help="Company name, Twitter handle (@username), or URL"
    )
    parser.add_argument(
        "--focus",
        help="Focus area: twitter, youtube, linkedin, launches, newsletter",
        default=None
    )
    parser.add_argument(
        "--output",
        help="Output file (default: stdout)",
        default=None
    )

    args = parser.parse_args()

    # Run research
    results = research_target(args.target, args.focus)

    # Output
    output_json = json.dumps(results, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
