#!/usr/bin/python3
"""Recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recurse function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data['after']

        for post in data.get('children'):
            hot_list.append(post['data']['title'])

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
