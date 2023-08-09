#!/usr/bin/python3
'''
Function that queries Reddit API and prints titles of the first 10 hot posts
'''
import requests


def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts
    '''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'alxapiadvanced'
    }
    params = {
        'limit': 10
    }
    response = requests\
        .get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        for get_data in hot_posts:
            title = get_data['data']['title']
            print(title)
    else:
        print(None)
