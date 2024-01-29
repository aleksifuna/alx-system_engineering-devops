#!/usr/bin/python3
"""Exports data related to specific user in CSV"""
import json
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

    todo_list = []
    for todo in todo_response.json():
        todo_dict = {}

        if todo.get("userId") == int(sys.argv[1]):
            todo_dict["username"] = name
            todo_dict["task"] = todo.get("title")
            todo_dict["completed"] = todo.get("completed")
            todo_list.append(todo_dict)
    user_dict = {}
    user_dict[sys.argv[1]] = todo_list

    with open(sys.argv[1] + ".json", "w") as f:
        json.dump(user_dict, f)
