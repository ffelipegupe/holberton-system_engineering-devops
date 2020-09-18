#!/usr/bin/python3
"""
Use of reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    """
    user_agent = {'User-Agent': 'User Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        return req.get('data').get('subscribers')
    return 0
