"""
Web utilities for page fetching and social link extraction.

Note: Web search is handled by the Claude agent's built-in WebSearch tool.
This module provides helper functions for direct page fetching.
"""

import requests
import re
from html import unescape


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def clean_html(html: str) -> str:
    """Remove HTML tags and clean up text."""
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = unescape(html)
    html = re.sub(r'\s+', ' ', html)
    return html.strip()


def fetch_page(url: str, max_chars: int = 5000) -> dict:
    """
    Fetch a web page and extract text content.

    Args:
        url: URL to fetch
        max_chars: Maximum characters to return

    Returns:
        dict with page title, text content, and metadata
    """
    result = {
        "url": url,
        "title": None,
        "content": None,
        "error": None
    }

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        html = response.text

        # Extract title
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
        if title_match:
            result["title"] = clean_html(title_match.group(1))

        # Extract meta description
        desc_match = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
            html, re.IGNORECASE
        )
        if desc_match:
            result["description"] = clean_html(desc_match.group(1))

        # Extract main content
        content_html = re.sub(
            r'<(header|footer|nav|aside)[^>]*>.*?</\1>',
            '', html, flags=re.DOTALL | re.IGNORECASE
        )

        content = clean_html(content_html)
        result["content"] = content[:max_chars]

    except requests.RequestException as e:
        result["error"] = str(e)

    return result


def find_social_links(url: str) -> dict:
    """
    Find social media links on a webpage.

    Args:
        url: URL to scan for social links

    Returns:
        dict with discovered social media profiles
    """
    social_patterns = {
        "twitter": r'https?://(?:www\.)?(?:twitter|x)\.com/([a-zA-Z0-9_]+)',
        "linkedin_company": r'https?://(?:www\.)?linkedin\.com/company/([a-zA-Z0-9-]+)',
        "linkedin_person": r'https?://(?:www\.)?linkedin\.com/in/([a-zA-Z0-9-]+)',
        "youtube": r'https?://(?:www\.)?youtube\.com/(?:c/|channel/|@)([a-zA-Z0-9_-]+)',
        "instagram": r'https?://(?:www\.)?instagram\.com/([a-zA-Z0-9_.]+)',
        "tiktok": r'https?://(?:www\.)?tiktok\.com/@([a-zA-Z0-9_.]+)',
        "github": r'https?://(?:www\.)?github\.com/([a-zA-Z0-9-]+)',
        "substack": r'https?://([a-zA-Z0-9-]+)\.substack\.com',
    }

    results = {
        "source_url": url,
        "profiles": {}
    }

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        html = response.text

        for platform, pattern in social_patterns.items():
            matches = re.findall(pattern, html, re.IGNORECASE)
            if matches:
                unique_matches = list(dict.fromkeys(matches))
                results["profiles"][platform] = unique_matches[0]

    except requests.RequestException as e:
        results["error"] = str(e)

    return results
