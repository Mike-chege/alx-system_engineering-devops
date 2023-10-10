#!/usr/bin/python3
"""
This function queries the Reddit API and
Prints the titles of the first 10 hot posts
Listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Gets the titles of the first ten hot posts
    """
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
