#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
"""

import requests
import sys

id = int(sys.argv[1])
user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
user = requests.get(user_url).json()

todo_url = 'https://jsonplaceholder.typicode.com/todos'
params = {'userId': id}
todos = requests.get(todo_url, params=params).json()
task = 0
NoCompleted_tasks = 0
completed_tasks = []
for todo in todos:
    task += 1
    # print(type(todos['completed']))
    if todo['completed'] is True:
        NoCompleted_tasks += 1
        completed_tasks.append(todo['title'])
print(
        "Employee {} is done with tasks({}/{}):".format(
            user['name'], NoCompleted_tasks, task))
for tasks in completed_tasks:
    print("\t {}".format(tasks))
