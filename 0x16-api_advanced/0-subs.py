#!/usr/bin/python3
"""
API request to Reddit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Get the number of subcribers in a subreddit
    """
    url = 'https://api.reddit.com/r/{}'.format(subreddit)
    sub_reddit = requests.get(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) \
                    # Gecko/20100101 Firefox/88.0'
    }
    sub_reddit = requests.get(url, headers=headers)
    if sub_reddit.status_code != 200:
        return 0
    subcribers = requests.get(
        'https://api.reddit.com/r/{}/about'.format(subreddit), headers=headers)
    return subcribers.json().get('data').get('subscribers')
