#!/usr/bin/python3
"""top-ten"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])

            for i in range(min(10, len(data))):
                print(data[i].get('data', {}).get('title'))
            return "OK"
        else:
            print(None)
            return "OK"

    except Exception:
        print(None)
        return "OK"
