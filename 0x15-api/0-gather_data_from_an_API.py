#!/usr/bin/python3
"""
This script returns information about a given employee (ID)
Using REST API
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    toDO = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [tl.get("title") for tl in toDO if tl.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(toDO)))
    [print("\t {}".format(complete)) for complete in completed]
