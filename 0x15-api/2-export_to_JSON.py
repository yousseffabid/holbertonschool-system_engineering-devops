#!/usr/bin/python3
"""export data in the CSV format"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    todo_list = requests.get(url + 'todos',
                             params={'userId': int(argv[1])}).json()
    user = requests.get(url + 'users/{}'.format(argv[1])).json()

    list_of_dic = []

    for task in todo_list:
        list_of_dic.append({'task': task.get('title'),
                            'completed': task.get('completed'),
                            'username': user.get('username')})

    result = {argv[1]: list_of_dic}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(result, f)
