#!/usr/bin/python3
"""
API request to get titles
"""

import requests
import sys


def top_ten(subreddit):
    """
    Get the top 10 hots in a subreddit by title
    """

    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) \
                    Gecko/20100101 Firefox/88.0'
            }
    params = {
            'limit': 10
            }
    sub_reddit = requests.get(
            url, headers=headers, allow_redirects=False, params=params)
    if sub_reddit.status_code != 200:
        return print(None)
    topTen = sub_reddit.json()
    children = topTen.get('data').get('children')
    for child in children:
        print(child.get('data').get('title'))
