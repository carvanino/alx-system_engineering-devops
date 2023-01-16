#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
"""

import requests
import sys

id = int(sys.argv[1])
user_url = 'https://jsonplaceholder.typicode.com/users'
u = requests.get(user_url)
u_dict = u.json()
for user in u_dict:
    if user['id'] == id:
        user_name = user['name']

todo_url = 'https://jsonplaceholder.typicode.com/todos'
t = requests.get(todo_url)
t_dict = t.json()
task = 0
NoCompleted_tasks = 0
completed_tasks = []
for todos in t_dict:
    if todos['userId'] == id:
        task += 1
        # print(type(todos['completed']))
        if todos['completed'] is True:
            NoCompleted_tasks += 1
            completed_tasks.append(todos['title'])
print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, NoCompleted_tasks, task))
for tasks in completed_tasks:
    print("\t {}".format(tasks))
