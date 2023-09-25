#!/usr/bin/python3
"""
This script returns information about a given employee (ID)
Using REST API
"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    try:
        employee_id = sys.argv[1]
    except:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        exit(1)

    url = base_url + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    name = user[0].get('name')

    url = base_url + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    completed = 0
    completed_tasks = []
    for obj in objs:
        if obj.get('completed'):
            completed_tasks.append(obj)
            completed += 1

    print("{} is done with tasks({}/{}):".format(name, completed, len(objs)))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
