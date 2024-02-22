#!/usr/bin/python3
""" Gather data from an API """
import csv
import requests
import sys


def export_to_csv():
    """Gather data from an api"""
    if len(sys.argv) <= 1:
        print("Usage: python3 0-gather_data_from_an_API.py <int>")
        exit(1)

    emp_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(f"{url}todos?userId={emp_id}")
    emp = requests.get(f"{url}users/{emp_id}")
    username = emp.json().get('username')

    with open(f"{emp_id}.csv", 'w', newline='') as csvfile:
        todowriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_ALL)
        todowriter.writerows([[emp_id, username, t.get('completed'),
                               t.get('title')] for t in todos.json()])


if __name__ == "__main__":
    export_to_csv()
