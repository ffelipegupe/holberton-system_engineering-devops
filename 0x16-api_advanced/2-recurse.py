#!/usr/bin/python3
"""
Use of reddit API
"""

import requests
import json
import sys


def recurse(subreddit, hot_list=[]):
    """
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    first_url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    user_agent = {'User-Agent'}
    if len(hot_list) == 0:
        url = first_url
    else:
        url = first_url + '?after={}_{}'.format(
            hot_list[-1].get('kind'), hot_list[-1].get('data').get('id'))
    rep = requests.get(url, headers=user_agent)
    j_rep = json.loads(rep.text)
    try:
        data = j_rep.get('data')
        children = data.get('children')
    except:
        return None
    if children is None or data is None or len(children) < 1:
        return hot_list
    hot_list.extend(children)
    return recurse(subreddit, hot_list)
