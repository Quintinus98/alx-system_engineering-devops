#!/usr/bin/python3
""" Gather data from an API """
import json
import requests
import sys


def export_to_json():
    """Gather data from an api"""
    if len(sys.argv) <= 1:
        print("Usage: python3 2-export_to_JSON.py <int>")
        exit(1)

    emp_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(f"{url}todos?userId={emp_id}")
    emp = requests.get(f"{url}users/{emp_id}")
    username = emp.json().get('username')

    json_list = []
    for todo in todos.json():
        json_list.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })
    json_object = json.dumps({emp_id: json_list})
    with open(f"{emp_id}.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    export_to_json()
