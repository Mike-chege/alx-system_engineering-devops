#!/usr/bin/python3
"""
This script returns information about a given employee (ID)
Using REST API
"""


if __name__ == "__main__":
    import sys
    import requests

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo_list = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    status = [tl.get("title") for tl in todo_list if tl.get("status") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(status), len(todo_list)))
    [print("\t {}".format(s)) for s in status]
