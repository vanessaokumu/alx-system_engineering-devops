#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "YourFriendlyNeighbourhood/1.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        except KeyError:
            return 0
    else:
        return 0
