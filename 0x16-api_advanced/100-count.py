#!/usr/bin/python3
"""
supplies a script that sends an api request to reddit
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    querries reddit API and prints the number of times aword in a list appears

    """
    if not word_count:
        for word in word_list:
            word_count[word] = 0
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
        return
    results = response.json()['data']
    for topic in results['children']:
        title = topic['data']['title'].lower()
        words = title.split()
        for word in word_list:
            count = words.count(word)
            word_count[word] += count

    if results['after'] is None:
        sorted_word_list = sorted(
                word_count.items(),
                key=lambda x: x[1],
                reverse=True
                )
        for key, value in sorted_word_list:
            if value != 0:
                print(key + ': ' + str(value))
        return
    after = results['after']
    return count_words(subreddit, word_list, after, word_count)
