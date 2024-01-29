#!/usr/bin/python3
"""Exports data related to specific user in CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    for user in user_response.json():
        if user.get("id") == int(sys.argv[1]):
            name = user.get("username")

    with open(sys.argv[1] + '.csv', 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todo_response.json():
            csv_data = []
            if todo.get("userId") == int(sys.argv[1]):
                csv_data.append(todo.get("userId"))
                csv_data.append(name)
                csv_data.append(todo.get("completed"))
                csv_data.append(todo.get("title"))

                write.writerow(csv_data)
