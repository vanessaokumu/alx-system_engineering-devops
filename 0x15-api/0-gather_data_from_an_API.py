#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"https://jsonplaceholder.typicode.com/todos"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch the employee's TODO list and user details
        todo_response = requests.get(todo_url, params={"userId": employee_id})
        user_response = requests.get(user_url)

        # Check if the requests were successful
        if todo_response.status_code != 200 or
        user_response.status_code != 200:
            print("Failed to retrieve data. Please check the employee ID.")
            return

        # Parse JSON data from the responses
        todo_data = todo_response.json()
        user_data = user_response.json()

        # Extract user details
        employee_name = user_data.get("name")

        # Calculate TODO list progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        # Display the progress information
        print(f"Employee {employee_name} is done with tasks
                ({completed_tasks}/{total_tasks}):"
              .format(employee_name, completed_tasks, total_tasks))

        # Display completed task titles
        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
