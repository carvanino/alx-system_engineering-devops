#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
and writes into a json file
"""

import json
import requests
import sys


if __name__ == '__main__':
    filename = "todo_all_employees.json"
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(user_url).json()
    # print(users)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todo_url).json()
    dict_ = {}
    # task_list = []
    for user in users:
        task_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                # dict_['USER_ID'] = user.get('id')
                tasks = {}
                tasks['task'] = todo.get('title')
                tasks['completed'] = todo.get('completed')
                tasks['username'] = user.get('username')
                task_list.append(tasks)
        dict_[user.get('id')] = task_list

    # print(task_list)
    # print(dict_)

    with open(filename, 'w') as j_file:
        json.dump(dict_, j_file)
        # j_file.write(j_string)
