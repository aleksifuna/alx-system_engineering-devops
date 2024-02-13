#!/usr/bin/python3
"""
supplies a script that sends an api request to reddit
"""
import requests


def top_ten(subreddit):
    """
    querries reddit API and prints the titles of th first 10 hot posts
    listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
            'User-Agent': 'MyApp/1.0 (by Aleksifuna)'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()['data']['children']
        for i in range(10):
            print(results[i]['data']['title'])
