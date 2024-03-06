#!/usr/bin/python3
"""Count function"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """Count function"""
    if word_counts is None:
        word_counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    after = data.get('after')

    for post in data.get('children'):
        title = post['data']['title']
        for word in word_list:
            if f" {word.lower()} " in title.lower():
                if word.lower() not in word_counts:
                    word_counts[word.lower()] = 0
                word_counts[word.lower()] += 1

    if after is not None:
        count_words(subreddit, word_list, after, word_counts)
    else:
        sorted_counts = sorted(word_counts.items())
        for word, count in sorted_counts:
            print(f"{word}: {count}")
