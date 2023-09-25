#!/usr/bin/python3
"""
This script export all employees
Data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requestsi

    url = "https://jsonplaceholder.typicode.com/"
    all_users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as json_FILE:
        json.dump({
            user.get("id"): [{
                "task": tl.get("title"),
                "completed": tl.get("completed"),
                "username": user.get("username")
            } for tl in requests.get(
                url + "todos",
                params={"userId": user.get("id")}).json()]
            for user in all_users}, json_FILE)
