#!/usr/bin/python3
"""
This script exports data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    userID = sys.argv[1]
    user = requests.get(url + "users/{}".format(userID)).json()
    user_name = user.get("username")
    toDO = requests.get(url + "todos", params={"userId": userID}).json()

    with open("{}.json".format(userID), "w") as json_FILE:
        json.dump({userID: [{
            "task": tl.get("title"),
            "completed": tl.get("completed"),
            "username": user_name
        } for tl in toDO]}, json_FILE)
