#!/usr/bin/python3
"""
API request to get list of all hot artcles by titles
"""

import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """
    Get the list of all hot articles in a subreddit by title
    """

    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) \
                    Gecko/20100101 Firefox/88.0'
    }
    params = {
        'after': after,
        'count': count
    }

    sub_reddit = requests.get(
        url, headers=headers, allow_redirects=False, params=params)
    if sub_reddit.status_code != 200:
        return None
    data = sub_reddit.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    children = data.get('children')
    # print(len(children))
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    for child in children:
        hot_list.append(child.get('data').get('title'))

    # if after is not None:
        # recurse(subreddit, hot_list, after, count)

    return hot_list
