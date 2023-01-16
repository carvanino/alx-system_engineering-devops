#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
and writes into a json file
"""

import json
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    filename = "{}.json".format(id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    user = requests.get(user_url).json()
    # print(user)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': id}
    todos = requests.get(todo_url, params=params).json()
    dict_ = {}
    task_list = []
    for todo in todos:
        # dict_['USER_ID'] = user.get('id')
        tasks = {}
        tasks['task'] = todo.get('title')
        tasks['completed'] = todo.get('completed')
        tasks['username'] = user.get('username')
        task_list.append(tasks)
    dict_[user.get('id')] = task_list

    print(task_list)
    print(dict_)

    with open(filename, 'w') as j_file:
        j_string = json.dumps(dict_)
        j_file.write(j_string)
