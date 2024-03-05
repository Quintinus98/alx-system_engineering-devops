#!/usr/bin/python3
"""Top ten"""
import requests


def top_ten(subreddit):
    """Get the top ten hottest post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': '0x16-api_advanced'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
