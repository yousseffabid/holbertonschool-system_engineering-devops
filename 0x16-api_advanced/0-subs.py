#!/usr/bin/python3
"""0-subs Module"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    if not subreddit:
        return 0
    url = "https://www.reddit.com"
    api_endpoint = f"/r/{subreddit}/about.json"
    request = requests.get(f"{url}{api_endpoint}", headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    return 0
