#!/usr/bin/python3
"""
supplies a function that sends api request to reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    sends a get request to reddits api and return the number of subsvribers
    in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            'User-Agent': 'MyApp/1.0 (by Aleksifuna)'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get('data')
        return results.get('subscribers')
    return 0
