#!/usr/bin/python3
"""Exports data related to specific user in CSV"""
import json
import requests

if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)
    user_dict = {}

    for user in user_response.json():
        todo_list = []
        for todo in todo_response.json():
            todo_dict = {}

            if todo.get("userId") == user.get("id"):
                todo_dict["username"] = user.get("username")
                todo_dict["task"] = todo.get("title")
                todo_dict["completed"] = todo.get("completed")
                todo_list.append(todo_dict)

        user_dict[user.get("id")] = todo_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(user_dict, f)
