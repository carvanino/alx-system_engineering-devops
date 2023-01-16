#!/usr/bin/python3
"""
Uses a REST API return information about employees TODO List progress
and writes into a csv file
"""

import csv
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    filename = "{}.csv".format(id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    user = requests.get(user_url).json()
    # print(user)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': id}
    todos = requests.get(todo_url, params=params).json()
    rows = []
    for todo in todos:
        row = []
        row.append(user.get('id'))
        row.append(user.get('name'))
        row.append(todo.get('completed'))
        row.append(todo.get('title'))
        rows.append(row)

    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TITLE']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # writer.writerow(fields)
        # writer.writeheader()
        writer.writerows(rows)
