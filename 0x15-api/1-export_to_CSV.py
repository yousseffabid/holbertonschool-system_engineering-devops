#!/usr/bin/python3
"""export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    todo_list = requests.get(url + 'todos',
                             params={'userId': int(argv[1])}).json()
    user = requests.get(url + 'users/{}'.format(argv[1])).json()

    username = user.get('username')

    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.writer(f)
        for task in todo_list:
            userid = task.get('userId')
            title = task.get('title')
            completed = task.get('completed')
            writer.writerow([userid, username, completed, title])
