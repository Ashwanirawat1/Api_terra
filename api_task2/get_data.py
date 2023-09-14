import base64

import requests
import json

# GitHub repository information
repo_owner = 'Ashwanirawat1'
repo_name = 'Api_terra'
file_path = 'api_task2/empljson.json'

# Set the GitHub API endpoint URL for the specific file in the repository
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

github_token = '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'

# Headers for the request
headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github.v3+json'  # Specify the GitHub API version
}

# Send an HTTP GET request to retrieve the JSON data
response = requests.get(api_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = json.loads(response.content)

    # Decode the base64 content and load it as JSON
    content_base64 = json_data['content']
    decoded_content = base64.b64decode(content_base64).decode('utf-8')
    employee_data = json.loads(decoded_content)

    # Print the retrieved JSON data
    print("Retrieved JSON data:")
    print(json.dumps(employee_data, indent=4))
else:
    print(f"Failed to retrieve JSON data. Status code: {response.status_code}")
