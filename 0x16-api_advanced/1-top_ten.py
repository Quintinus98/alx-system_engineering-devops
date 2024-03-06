#!/usr/bin/python3
"""Top ten function"""
import requests


def top_ten(subreddit):
    """Top ten function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 9}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')

        for post in data.get('children'):
            print(post['data']['title'])
    else:
        print(None)
