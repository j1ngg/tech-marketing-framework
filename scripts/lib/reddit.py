"""
Reddit public JSON API integration

Reddit exposes a public JSON API by appending .json to any URL.
No authentication required for public subreddits and posts.

Rate limit: ~60 requests/minute without auth
"""

import requests
from typing import Optional
from urllib.parse import quote


HEADERS = {
    "User-Agent": "how-they-market/1.0 (research tool)"
}


def search_reddit(query: str, limit: int = 25, sort: str = "relevance", time: str = "year") -> dict:
    """
    Search Reddit for posts mentioning a company/person.

    Args:
        query: Search term (company name, product, person)
        limit: Max results (default 25, max 100)
        sort: relevance, hot, top, new, comments
        time: hour, day, week, month, year, all

    Returns:
        dict with posts and stats
    """
    url = f"https://www.reddit.com/search.json"
    params = {
        "q": query,
        "limit": min(limit, 100),
        "sort": sort,
        "t": time
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=15)

        if response.status_code == 200:
            data = response.json()
            posts = []

            for child in data.get("data", {}).get("children", []):
                post = child.get("data", {})
                posts.append({
                    "title": post.get("title"),
                    "subreddit": post.get("subreddit"),
                    "author": post.get("author"),
                    "score": post.get("score", 0),
                    "num_comments": post.get("num_comments", 0),
                    "url": f"https://reddit.com{post.get('permalink', '')}",
                    "created_utc": post.get("created_utc"),
                    "selftext": post.get("selftext", "")[:500] if post.get("selftext") else None
                })

            return {
                "query": query,
                "posts": posts,
                "stats": {
                    "total_posts": len(posts),
                    "total_score": sum(p["score"] for p in posts),
                    "total_comments": sum(p["num_comments"] for p in posts),
                    "top_subreddits": _get_top_subreddits(posts)
                },
                "error": None
            }
        else:
            return {
                "query": query,
                "posts": [],
                "stats": {},
                "error": f"Reddit returned status {response.status_code}"
            }

    except requests.RequestException as e:
        return {
            "query": query,
            "posts": [],
            "stats": {},
            "error": str(e)
        }


def get_subreddit_posts(subreddit: str, sort: str = "hot", limit: int = 25) -> dict:
    """
    Get posts from a specific subreddit.

    Args:
        subreddit: Subreddit name (without r/)
        sort: hot, new, top, rising
        limit: Max posts to return

    Returns:
        dict with posts
    """
    url = f"https://www.reddit.com/r/{quote(subreddit)}/{sort}.json"
    params = {"limit": min(limit, 100)}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=15)

        if response.status_code == 200:
            data = response.json()
            posts = []

            for child in data.get("data", {}).get("children", []):
                post = child.get("data", {})
                posts.append({
                    "title": post.get("title"),
                    "author": post.get("author"),
                    "score": post.get("score", 0),
                    "num_comments": post.get("num_comments", 0),
                    "url": f"https://reddit.com{post.get('permalink', '')}",
                    "created_utc": post.get("created_utc")
                })

            return {
                "subreddit": subreddit,
                "posts": posts,
                "error": None
            }
        else:
            return {
                "subreddit": subreddit,
                "posts": [],
                "error": f"Reddit returned status {response.status_code}"
            }

    except requests.RequestException as e:
        return {
            "subreddit": subreddit,
            "posts": [],
            "error": str(e)
        }


def _get_top_subreddits(posts: list, limit: int = 5) -> list:
    """Get the most common subreddits from a list of posts."""
    subreddit_counts = {}
    for post in posts:
        sub = post.get("subreddit")
        if sub:
            subreddit_counts[sub] = subreddit_counts.get(sub, 0) + 1

    sorted_subs = sorted(subreddit_counts.items(), key=lambda x: x[1], reverse=True)
    return [{"subreddit": sub, "count": count} for sub, count in sorted_subs[:limit]]
