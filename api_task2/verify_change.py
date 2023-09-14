import requests
import base64
import json

def update_employee_attribute(username, access_token, repo_name, file_path, employee_index, attribute_name, new_value):
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
                employee = json_data[employee_index]

                # Print the original data before the update
                print(f"Original Data for Employee {employee_index + 1}:\n{employee}")

                # Update the specified attribute with the new value
                if attribute_name in employee:
                    employee[attribute_name] = new_value

                    # Encode the updated JSON data to Base64
                    updated_content = base64.b64encode(json.dumps(json_data).encode('utf-8')).decode('utf-8')

                    # Create a data payload for the update request
                    update_data = {
                        "message": f"Update {attribute_name} of employee {employee_index}",
                        "content": updated_content,
                        "sha": current_content["sha"]
                    }

                    # Make a PUT request to update the file
                    update_response = requests.put(base_url, headers=headers, json=update_data)

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
            print("No content found in the response.")
    else:
        print(f"Failed to fetch file content. Status code: {response.status_code}")

# to update the designation of the fifth employee
update_employee_attribute("Ashwanirawat1", "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", "Api_terra", "api_task2/empljson.json", 4, "designation", "Project Manager")
