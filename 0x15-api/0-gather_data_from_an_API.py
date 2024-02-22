#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys


def gather_data():
    """Gather data from an api"""
    if len(sys.argv) <= 1:
        print("Usage: python3 0-gather_data_from_an_API.py <int>")
        exit(1)

    emp_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(f"{url}todos?userId={emp_id}")
    emp = requests.get(f"{url}users/{emp_id}")
    name = emp.json().get('name')
    todo_count = 0
    todo_completed = []
    for todo in todos.json():
        if todo.get('completed') is True:
            todo_count += 1
            todo_completed.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, todo_count, len(todos.json())))
    for tasks in todo_completed:
        print(f"\t {tasks}")


if __name__ == "__main__":
    gather_data()
