#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests


def get_all_employee_todo_progress():
    # Define the API endpoint URL for todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        # Fetch all TODOs
        todo_response = requests.get(todos_url)

        # Check if the request was successful
        if todo_response.status_code != 200:
            print("Failed to retrieve data from the API.")
            return

        # Parse JSON data from the response
        todo_data = todo_response.json()

        # Create a dictionary to store tasks by user ID
        tasks_by_user = {}

        # Iterate through the TODOs and organize them by user ID
        for task in todo_data:
            user_id = task["userId"]
            username = task["title"]
            task_title = task["title"]
            task_completed = task["completed"]

            if user_id not in tasks_by_user:
                tasks_by_user[user_id] = []

            tasks_by_user[user_id].append({"username": username,
                "task": task_title, "completed": task_completed})

        # Create a JSON file for all employees
        json_filename = "todo_all_employees.json"
        with open(json_filename, "w") as json_file:
            json.dump(tasks_by_user, json_file, indent=4)

        print(f"JSON file '{json_filename}' has been created successfully!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_all_employee_todo_progress()
