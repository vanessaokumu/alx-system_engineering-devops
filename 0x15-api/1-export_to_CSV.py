#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

import csv
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

        # Create a CSV file for the user
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write each task to the CSV file
            for task in todo_data:
                task_id = task["id"]
                task_title = task["title"]
                task_completed = task["completed"]
                csv_writer.writerow([user_id, username, task_completed, task_title])

        print(f"CSV file '{csv_filename}' has been created successfully!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
