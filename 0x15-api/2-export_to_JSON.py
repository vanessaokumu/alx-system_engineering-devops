#!/usr/bin/python3
"""
Using what you did in the task #0, 
extend your Python script to export data in the JSON format.
"""

import json
import requests


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URLs
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch the employee's TODO list and user details
        todo_response = requests.get(todos_url)
        user_response = requests.get(user_url)

        # Check if the requests were successful
        if todo_response.status_code != 200 or user_response.status_code != 200:
            print("Failed to retrieve data. Please check the employee ID.")
            return

        # Parse JSON data from the responses
        todo_data = todo_response.json()
        user_data = user_response.json()

        # Extract user details
        user_id = user_data.get("id")
        username = user_data.get("username")

        # Create a list of tasks in the specified JSON format
        tasks = [{"task": task["title"], "completed": task["completed"],
            "username": username} for task in todo_data]

        # Create a JSON file for the user
        json_filename = f"{user_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump({user_id: tasks}, json_file, indent=4)

        print(f"JSON file '{json_filename}' has been created successfully!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
