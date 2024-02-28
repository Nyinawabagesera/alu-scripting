#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid issues
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            # If the request was not successful, return 0
            return 0
    except Exception as e:
        # Handle exceptions, e.g., invalid subreddit or network issues
        print(f"Error: {e}")
        return 0

# Example usage:
subreddit_name = "learnpython"
subscribers_count = number_of_subscribers(subreddit_name)

print(f"The number of subscribers in the subreddit {subreddit_name} is: {subscribers_count}")

