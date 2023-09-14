import requests
import base64
import json

# GitHub repository information
github_username = "Ashwanirawat1"
access_token = "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"
repo_name = "Api_terra"
file_path = "api_task2/empljson.json"

# Define the base URL for the repository content API
base_url = f"https://api.github.com/repos/{github_username}/{repo_name}/contents/{file_path}"

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

        # Modify the JSON data as needed
        json_data[4]["designation"] = "Manager"

        # Encode the updated JSON data to Base64
        updated_content = base64.b64encode(json.dumps(json_data).encode('utf-8')).decode('utf-8')

        # Create a data payload for the update request
        update_data = {
            "message": "Update JSON file",
            "content": updated_content,
            "sha": current_content["sha"]
        }

        # Make a PUT request to update the file
        update_response = requests.put(base_url, headers=headers, json=update_data)

        if update_response.status_code == 200:
            print("File updated successfully.")
        else:
            print(f"Failed to update file. Status code: {update_response.status_code}")
    else:
        print("No content found in the response.")
else:
    print(f"Failed to fetch file content. Status code: {response.status_code}")
