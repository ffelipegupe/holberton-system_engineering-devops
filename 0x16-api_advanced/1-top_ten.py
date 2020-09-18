#!/usr/bin/python3
"""
Use of reddit API
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    user_agent = {'User-Agent': 'User Agent'}
    url = 'https://www.reddit.com/r/{}/top/.json?limit=10'.format(subreddit)
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        children = data.get('children')
        if data is not None and children is not None:
            for pst in children:
                p_data = pst.get('data')
                title = p_data.get('title')
                print(title)
        else:
            print("None")
            return None
