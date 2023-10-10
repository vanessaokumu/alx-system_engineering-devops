#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. 
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    if not hot_list:
        return None

    # Define the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "YourFriendlyNeighbourhood/1.0 (by YourFriendly)"
    }

    # "after" parameter for pagination
    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            
            for post in posts:
                hot_list.append(post["data"]["title"])

            after = data["data"]["after"]
            if after:
                # Recursively call the function with the "after" parameter
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except KeyError:
            return None
    else:
        return None
