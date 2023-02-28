#!/usr/bin/python3
""" Program that use Reddit API and query How many subs are there"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number
    of subscribers """
    url_subs = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    hdr = {'User-Agent': 'My User Agent'}
    req = requests.get(url_subs, headers=hdr, allow_redirects=False)

    if (req.status_code == 200):
        req_json = req.json()
        count = req_json['data']['subscribers']
        return (count)
    return (0)
