#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

from collections import Counter
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()
    
    # If word_list is empty, print the counts in descending order
    if not word_list:
        for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word.lower()}: {count}")
        return

    # If subreddit is invalid or no posts match, print nothing
    if subreddit is None:
        return

    # Define the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "YourFriendlyNeighbourhood/1.0 (by YourFriendly)"
    }

    # Include the "after" parameter for pagination if it's provided
    if after:
        url += f"&after={after}"

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            
            # Extract the titles of the hot posts
            titles = [post["data"]["title"].lower() for post in posts]

            for word in word_list:
                counts[word] += titles.count(word.lower())

            after = data["data"]["after"]
            if after:
                return count_words(subreddit, word_list, after, counts)
        except KeyError:
            return None
