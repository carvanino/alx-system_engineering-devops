#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
"""

import csv
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    filename = "{}.csv".format(id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    user = requests.get(user_url).json()
    print(user)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': id}
    todos = requests.get(todo_url, params=params).json()
    task = 0
    NoCompleted_tasks = 0
    completed_tasks = []
    for todo in todos:
        task += 1
        # print(type(todos['completed']))
        if todo.get('completed') is True:
            NoCompleted_tasks += 1
            completed_tasks.append(todo.get('title'))
    print(
            "Employee {} is done with tasks({}/{}):".format(
                user.get('name'), NoCompleted_tasks, task))
    for tasks in completed_tasks:
        print("\t {}".format(tasks))

    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TITLE']
    col_vals = []
    #for key, val in user:
    #col_vals.append(str(id))
    col_vals.append(user.get('name'))
    col_vals.append(todo.get('completed'))
    col_vals.append(todo.get('title'))
    print(col_vals)
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(col_vals)


