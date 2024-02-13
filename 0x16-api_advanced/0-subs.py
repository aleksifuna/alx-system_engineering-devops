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
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {
            'User-Agent': 'MyApp/1.0 (by Aleksifuna)'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
