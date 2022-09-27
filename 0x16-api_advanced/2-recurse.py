#!/usr/bin/python3
"""2-recurse Module"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit."""
    if not subreddit:
        return None
    url = "https://www.reddit.com"
    endpoint = "/r/{}/hot.json?limit=100&after={}".format(subreddit, after)

    request = requests.get("{}{}".format(url, endpoint),
                           headers={'User-agent': 'Mozilla/5.0'},
                           allow_redirects=False)

    if request.status_code == 200:
        children = request.json().get('data').get('children')
        after = request.json().get('data').get('after')

        for elem in children:
            hot_list.append(elem.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list

    return None
