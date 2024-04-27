#!/usr/bin/python3
"""Module to create JSON of all employees tasks"""
import json
import requests

EMPLOYEE_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/users').json()

todo_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/todos').json()

USER_DATA = {}

with open('todo_all_employees.json', 'w') as jsonfile:
    for employees in EMPLOYEE_DATA:
        USER_ID = employees.get("id")
        USERNAME = employees.get("username")

        USER_DATA[USER_ID] = []

        for tasks in todo_DATA:
            if tasks.get("userId") == USER_ID:
                task_data = {
                    "username": USERNAME,
                    "task": tasks.get("title"),
                    "completed": tasks.get("completed")
                }
                USER_DATA[USER_ID].append(task_data)

    json.dump(USER_DATA, jsonfile)
