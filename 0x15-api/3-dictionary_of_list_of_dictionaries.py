#!/usr/bin/python3
"""export data in the json format"""

import json
import requests

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(url + 'users').json()

    result = {}

    for user in users:
        todo_list = requests.get(url + "todos",
                                 params={"userId": user.get("id")}).json()
        list_of_dic = []
        for task in todo_list:
            list_of_dic.append({'username': user.get('username'),
                                'task': task.get('title'),
                                'completed': task.get('completed')})
        result[user.get('id')] = list_of_dic

    with open('todo_all_employees.json', 'w') as f:
        json.dump(result, f)
