import requests
import base64
import json

def delete_employee(username, access_token, repo_name, file_path, employee_index):
    # Define the base URL for the repository content API
    base_url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}"

    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Fetch the current content of the JSON file
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        # Parse the response JSON
        current_content = response.json()

        if "content" in current_content:
            # Get the existing content as a string
            base64_content = current_content["content"]
            decoded_content = base64.b64decode(base64_content).decode('utf-8')
            json_data = json.loads(decoded_content)

            if 0 <= employee_index < len(json_data):
                # Access the specified employee data
                deleted_employee = json_data.pop(employee_index)
                print(deleted_employee)
                # Encode the updated JSON data to Base64 after deletion
                updated_content = base64.b64encode(json.dumps(json_data).encode('utf-8')).decode('utf-8')

                # Create a data payload for the update request (delete operation)
                update_data = {
                    "message": f"Delete Employee {employee_index + 1}",
                    "content": updated_content,
                    "sha": current_content["sha"]
                }

                # Make a PUT request to update the file (effectively deleting the employee data)
                update_response = requests.put(base_url, headers=headers, json=update_data)

                if update_response.status_code == 200:
                    print(f"Employee {employee_index + 1} deleted successfully.")
                    # Print the deleted employee data
                    print(f"Deleted Data for Employee {employee_index + 1}:\n{deleted_employee}")
                else:
                    print(f"Failed to delete Employee {employee_index + 1}.")
            else:
                print(f"Employee index {employee_index} out of range.")
        else:
            print("No content found in the response.")
    else:
        print(f"Failed to fetch file content. Status code: {response.status_code}")

# Example usage to delete the 10th employee
delete_employee("Ashwanirawat1", "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", "Api_terra", "api_task2/employeejso.json", 9)
