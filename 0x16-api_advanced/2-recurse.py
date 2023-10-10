#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    # Base case: If the subreddit is invalid, return None.
    if subreddit is None:
        return None
    
    # Define the Reddit API URL for fetching hot articles.
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Define the headers to mimic a User-Agent (Reddit requires this header).
    headers = {"User-Agent": "MyRedditScraper"}
    
    # Define the parameters for the API request, including 'after' for pagination.
    params = {"limit": 100, "after": after}
    
    # Make the API request.
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful.
    if response.status_code != 200:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'.")
        return None
    
    # Parse the JSON response.
    data = response.json()
    
    # Extract the 'children' containing the article data from the response.
    children = data.get("data", {}).get("children", [])
    
    # Iterate through the articles and add their titles to the hot_list.
    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            hot_list.append(title)
    
    # Check if there are more pages (more articles) to retrieve.
    after = data.get("data", {}).get("after")
    
    # If there are more pages, recursively call the function.
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        # If there are no more pages, return the hot_list.
        return hot_list

# Example usage:
subreddit_name = "python"
hot_articles = recurse(subreddit_name)

if hot_articles is not None:
    print(f"Hot articles in r/{subreddit_name}:")
    for idx, title in enumerate(hot_articles, start=1):
        print(f"{idx}. {title}")
else:
    print(f"No results found for subreddit '{subreddit_name}' or it is invalid.")

