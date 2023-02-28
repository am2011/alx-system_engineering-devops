#!/usr/bin/python3
"""Query How many subs are there? and list the
top ten with recursion"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""
    url_hot = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    hdr = {'User-Agent': 'My User Agent'}
    req = requests.get(url_hot, headers=hdr, allow_redirects=False)

    if (req.status_code == 200):
        req_json = req.json()
        data_list = req_json['data']['children']
        for i in data_list:
            hot_list.append(i['data']['title'])
        after = req_json['data']['after']
        if (after is not None):
            recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    else:
        return (None)
    return (hot_list)
