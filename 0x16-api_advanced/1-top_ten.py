#!/usr/bin/python3
"""1-top_ten Module"""
import requests


def top_ten(subreddit):
    """queries Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit."""
    if not subreddit:
        print('None')
    url = "https://www.reddit.com"
    api_endpoint = f"/r/{subreddit}/hot.json?limit=10"
    req = requests.get(f"{url}{api_endpoint}", headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    if req.status_code == 200:
        for el in req.json().get('data').get('children'):
            if el.get('data').get('title'):
                print(el.get('data').get('title'))
    else:
        print('None')
