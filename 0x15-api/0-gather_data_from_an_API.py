#!/usr/bin/python3
"""sends API request to https://jsonplaceholder.typicode.com/todos"""
import requests
import sys

completed = 0
total = 0
titles = []

if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)
    for user in user_response.json():
        if user.get("id") == int(sys.argv[1]):
            name = user.get("name")
    if todo_response.status_code == 200:
        todo_list = todo_response.json()
        for todo in todo_list:
            if todo.get("userId") == int(sys.argv[1]):
                total += 1
                if todo.get("completed") is True:
                    completed += 1
                    titles.append(todo.get("title"))
        print(f"Employee {name} is done with tasks({completed}/{total}):")
        for title in titles:
            print(f"\t {title}")
