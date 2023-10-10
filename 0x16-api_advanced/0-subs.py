#!/usr/bin/python3
"""
This function queries the Reddit API and
Returns the number of subscribers
(not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """
    Calling api to return the number of subscribers
    """
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }

    response = requests.get(base_url, headers=headers, allow_redirects=False)
    # If response not found(404) return 0
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
