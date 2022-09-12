#!/usr/bin/python3
""" for a given employee ID,
    returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    todo_list = requests.get(url + 'todos',
                             params={'userId': int(argv[1])}).json()
    user = requests.get(url + 'users/{}'.format(argv[1])).json()

    user_name = user.get('name')
    number_of_done_tasks = 0
    completed_tasks = []

    for i in range(len(todo_list)):
        if todo_list[i].get('completed') is True:
            number_of_done_tasks += 1
            completed_tasks.append(todo_list[i].get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, number_of_done_tasks, len(todo_list)))

    for i in range(len(completed_tasks)):
        print('\t {}'.format(completed_tasks[i]))
