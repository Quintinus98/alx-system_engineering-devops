#!/usr/bin/python3
""" Gather data from an API """
import json
import requests


def export_all_to_json():
    """Gather data from an api"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users/").json()

    records = {}
    user_data = []
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        todos = requests.get(f"{url}todos?userId={user_id}").json()
        for todo in todos:
            user_data.append({
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
        records[user_id] = user_data

    json_object = json.dumps(records)
    with open("todo_all_employees.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    export_all_to_json()
