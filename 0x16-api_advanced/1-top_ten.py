#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "YourFriendlyNeighbourhood/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            posts = data["data"]["children"]
            
            """Print the titles of the hot posts"""
            for post in posts:
                print(post["data"]["title"])
        except KeyError:
            print("None")
    else:
        print("None")
