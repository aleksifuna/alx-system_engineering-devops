#!/usr/bin/python3
"""
supplies a script that sends an api request to reddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    querries reddit API and returns a list of hot topics in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
            'User-Agent': 'MyApp/1.0 (by Aleksifuna)'
            }
    params = {
            'after': after
            }
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
    if response.status_code != 200:
        return None
    results = response.json()['data']
    for topic in results['children']:
        hot_list.append(topic['data']['title'])
    if results['after'] is None:
        return hot_list
    after = results['after']
    return recurse(subreddit, hot_list, after)
