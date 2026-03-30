"""
Hacker News search via Algolia API (free, no auth required)

API docs: https://hn.algolia.com/api
"""

import requests
from typing import Optional
from datetime import datetime, timedelta


HN_API_BASE = "https://hn.algolia.com/api/v1"


def search_hackernews(query: str, days: int = 90, max_results: int = 20) -> dict:
    """
    Search Hacker News for mentions of a target.

    Args:
        query: Search term (company name, product, person)
        days: How far back to search (default 90 days)
        max_results: Maximum number of results to return

    Returns:
        dict with stories and comments mentioning the target
    """
    results = {
        "query": query,
        "stories": [],
        "comments": [],
        "stats": {
            "total_stories": 0,
            "total_comments": 0,
            "total_points": 0,
            "top_story_points": 0
        }
    }

    # Calculate timestamp for date filter
    since_timestamp = int((datetime.now() - timedelta(days=days)).timestamp())

    try:
        # Search stories
        stories_response = requests.get(
            f"{HN_API_BASE}/search",
            params={
                "query": query,
                "tags": "story",
                "numericFilters": f"created_at_i>{since_timestamp}",
                "hitsPerPage": max_results
            },
            timeout=10
        )
        stories_response.raise_for_status()
        stories_data = stories_response.json()

        for hit in stories_data.get("hits", []):
            story = {
                "title": hit.get("title"),
                "url": hit.get("url"),
                "author": hit.get("author"),
                "points": hit.get("points", 0),
                "num_comments": hit.get("num_comments", 0),
                "created_at": hit.get("created_at"),
                "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
            }
            results["stories"].append(story)
            results["stats"]["total_points"] += story["points"] or 0
            if (story["points"] or 0) > results["stats"]["top_story_points"]:
                results["stats"]["top_story_points"] = story["points"]

        results["stats"]["total_stories"] = len(results["stories"])

        # Search comments (what people are saying about them)
        comments_response = requests.get(
            f"{HN_API_BASE}/search",
            params={
                "query": query,
                "tags": "comment",
                "numericFilters": f"created_at_i>{since_timestamp}",
                "hitsPerPage": max_results
            },
            timeout=10
        )
        comments_response.raise_for_status()
        comments_data = comments_response.json()

        for hit in comments_data.get("hits", []):
            comment = {
                "text": hit.get("comment_text", "")[:500],  # Truncate long comments
                "author": hit.get("author"),
                "points": hit.get("points"),
                "created_at": hit.get("created_at"),
                "story_id": hit.get("story_id"),
                "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
            }
            results["comments"].append(comment)

        results["stats"]["total_comments"] = len(results["comments"])

    except requests.RequestException as e:
        results["error"] = str(e)

    return results


def get_user_submissions(username: str) -> Optional[dict]:
    """
    Get a HN user's submissions and karma.

    Args:
        username: Hacker News username

    Returns:
        dict with user stats and recent submissions
    """
    try:
        user_response = requests.get(
            f"{HN_API_BASE}/users/{username}",
            timeout=10
        )
        user_response.raise_for_status()
        return user_response.json()
    except requests.RequestException:
        return None
