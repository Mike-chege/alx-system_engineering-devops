#!/usr/bin/python3
"""
This script exports data in the CSV format
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    userID = sys.argv[1]
    user = requests.get(url + "users/{}".format(userID)).json()
    user_name = user.get("username")
    toDO = requests.get(url + "todos", params={"userId": userID}).json()

    with open("{}.csv".format(userID), "w", newline="") as csv_FILE:
        writer = csv.writer(csv_FILE, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userID, user_name, t.get("completed"), t.get("title")]
        ) for t in toDO]
