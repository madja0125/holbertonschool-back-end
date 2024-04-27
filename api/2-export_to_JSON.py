#!/usr/bin/python3
"""Module to create CSV"""
import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user_num = int(user_id)

    EMPLOYEE_DATA = requests.get(
        f'https://jsonplaceholder.typicode.com/users?Id={user_id}').json()

    todo_DATA = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

    EMPLOYEE_NAME = EMPLOYEE_DATA[int(user_id)-1].get("name")
    USER_ID = EMPLOYEE_DATA[int(user_id)-1].get("id")
    USERNAME = EMPLOYEE_DATA[int(user_id)-1].get("username")

    with open(f'{user_id}.json', 'w') as jsonfile:
        USER_DATA = {USER_ID: []}

        for tasks in todo_DATA:
            task_data = {
                "task": tasks.get('title'),
                "completed": tasks.get('completed'),
                "username": USERNAME}
            USER_DATA[USER_ID].append(task_data)

        json.dump(USER_DATA, jsonfile)
