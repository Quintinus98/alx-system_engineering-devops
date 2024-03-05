#!/usr/bin/python3
"""Returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return (0)
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    return response.json().get('data', {}).get('subscribers', 0)
