import requests
import base64
import json
from Token import api_token

class GitHubJsonFileManager:
    def __init__(self, repo_owner, repo_name, file_path):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.file_path = file_path
        self.github_token = api_token.Api_token.git_token
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        self.headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def create_json_file(self, file_content, commit_message="Create new JSON file", branch="main"):
        # Encode the file content to base64
        content_base64 = base64.b64encode(file_content.encode()).decode()

        # Payload for creating the new file
        payload = {
            "message": commit_message,
            "content": content_base64,
            "branch": branch
        }

        # Send a PUT request to create the new file
        response = requests.put(self.base_url, json=payload, headers=self.headers)

        if response.status_code == 201:
            print("File created successfully!")
        else:
            print(f"Failed to create file. Status code: {response.status_code}")

    def get_json_content(self):
        # Send an HTTP GET request to retrieve the JSON data
        response = requests.get(self.base_url, headers=self.headers)

        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()

            # Decode the base64 content and load it as JSON
            content_base64 = json_data['content']
            decoded_content = base64.b64decode(content_base64).decode('utf-8')

            try:
                employee_data = json.loads(decoded_content)
                return employee_data, json_data['sha']
            except json.JSONDecodeError as e:
                print("Failed to decode JSON content:")
                print(decoded_content)
                print("Error:", str(e))
                return None, None
        else:
            print(f"Failed to retrieve JSON data. Status code: {response.status_code}")
            return None, None

    def update_employee_attribute(self, employee_index, attribute_name, new_value, sha):
        # Fetch the current content of the JSON file
        current_content, current_sha = self.get_json_content()

        if current_content is not None:
            if 0 <= employee_index < len(current_content):
                # Access the specified employee data
                employee = current_content[employee_index]

                # Print the original data before the update
                print(f"Original Data for Employee {employee_index + 1}:\n{employee}")

                # Update the specified attribute with the new value
                if attribute_name in employee:
                    employee[attribute_name] = new_value

                    # Encode the updated JSON data to Base64
                    updated_content = base64.b64encode(json.dumps(current_content).encode('utf-8')).decode('utf-8')

                    # Create a data payload for the update request
                    update_data = {
                        "message": f"Update {attribute_name} of employee {employee_index}",
                        "content": updated_content,
                        "sha": sha
                    }

                    # Make a PUT request to update the file
                    update_response = requests.put(self.base_url, headers=self.headers, json=update_data)

                    if update_response.status_code == 200:
                        print(f"\n{attribute_name} of Employee {employee_index + 1} updated successfully.")
                        # Print the updated data
                        print(f"Updated Data for Employee {employee_index + 1}:\n{employee}")
                    else:
                        print(f"Failed to update {attribute_name} of Employee {employee_index + 1}.")
                else:
                    print(f"Attribute {attribute_name} not found for Employee {employee_index + 1}.")
            else:
                print(f"Employee index {employee_index} out of range.")
        else:
            print("Cannot update. No valid JSON data.")

    def delete_employee(self, employee_index):
        # Fetch the current content of the JSON file
        current_content, current_sha = self.get_json_content()

        if current_content is not None:
            if 0 <= employee_index < len(current_content):
                # Access the specified employee data
                deleted_employee = current_content.pop(employee_index)
                print(deleted_employee)
                # Encode the updated JSON data to Base64 after deletion
                updated_content = base64.b64encode(json.dumps(current_content).encode('utf-8')).decode('utf-8')

                # Create a data payload for the update request (delete operation)
                update_data = {
                    "message": f"Delete Employee {employee_index + 1}",
                    "content": updated_content,
                    "sha": current_sha
                }

                # Make a PUT request to update the file (effectively deleting the employee data)
                update_response = requests.put(self.base_url, headers=self.headers, json=update_data)

                if update_response.status_code == 200:
                    print(f"Employee {employee_index + 1} deleted successfully.")
                    # Print the deleted employee data
                    print(f"Deleted Data for Employee {employee_index + 1}:\n{deleted_employee}")
                else:
                    print(f"Failed to delete Employee {employee_index + 1}.")
            else:
                print(f"Employee index {employee_index} out of range.")
        else:
            print("Cannot delete. No valid JSON data.")

    def verify_deletion_and_list_employees(self):
        # Retrieve JSON content again after the deletion
        retrieved_data, _ = self.get_json_content()

        if retrieved_data:
            print("\nUpdated JSON data (after deletion):")
            print(json.dumps(retrieved_data, indent=4))
            print(f"\nTotal Employees after deletion: {len(retrieved_data)}")
        else:
            print("\nFailed to retrieve JSON data after deletion.")


# Create a new instance of the GitHubJsonFileManager class
manager = GitHubJsonFileManager("Ashwanirawat1", "Api_terra", "api_task2/emp.json")

# create a new JSON file
new_json_data = '''[
    {"emp_id": 1, "name": "John Doe", "age": 30, "designation": "Software Engineer"},
    {"emp_id": 2, "name": "Jane Smith", "age": 28, "designation": "Data Analyst"},
    {"emp_id": 3, "name": "David Johnson", "age": 35, "designation": "Product Manager"},
    {"emp_id": 4, "name": "Emily Davis", "age": 27, "designation": "UX Designer"},
    {"emp_id": 5, "name": "Michael Wilson", "age": 32, "designation": "Frontend Developer"},
    {"emp_id": 6, "name": "Sophia Brown", "age": 29, "designation": "Backend Developer"},
    {"emp_id": 7, "name": "Olivia Lee", "age": 33, "designation": "Data Scientist"},
    {"emp_id": 8, "name": "William Moore", "age": 31, "designation": "DevOps Engineer"},
    {"emp_id": 9, "name": "Ava Taylor", "age": 26, "designation": "QA Tester"},
    {"emp_id": 10, "name": "Liam Anderson", "age": 34, "designation": "Project Manager"}
]'''
manager.create_json_file(new_json_data, commit_message="Update employee data", branch="main")

# retrieve JSON content and SHA
retrieved_data, sha = manager.get_json_content()
if retrieved_data:
    print("Retrieved JSON data:")
    print(json.dumps(retrieved_data, indent=4))

    # update the designation of the fifth employee
    manager.update_employee_attribute(1, "designation", "Project Manager", sha)

    # delete an employee
    manager.delete_employee(2)

    # Verify the deletion and list employees again
    manager.verify_deletion_and_list_employees()
