#!/usr/bin/python3
"""Module to query Reddit API and get top 10 hot
 posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit"""
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'linux:custom_reddit_client:v1.0 (by /u/custom_client)'
    }

    # Parameters to limit to 10 posts and avoid redirects
    params = {
        'limit': 10
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)

        # Check if subreddit exists (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json().get('data', {}).get('children', [])

            # Print titles of first 10 posts
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # If subreddit is invalid or other error occurs
            print(None)

    except Exception:
        # Handle any other errors that might occur
        print(None)
