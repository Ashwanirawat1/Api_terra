import requests
import json
import Token

# token = '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'
github_token = Token.api_token.Api_token.git_token
# Set the GitHub repository URL
repo_owner = 'Ashwanirawat1'
repo_name = 'demo2_re'

# Set the GitHub API endpoint URL for the specific repository
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

# Define the new repository data
new_data = {
    "name": "demo_api",
    "id": 2,
    "category": {
        "id": 2,
        "name": "string"
    },
    "name1": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 3,
            "name": "string"
        }
    ],
    "status": "available"
}

# Convert the new data to JSON format
json_data = json.dumps(new_data)

# Define the headers with the token and content type
headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/json',
}

# Send a PATCH request to update the repository
response = requests.patch(url, headers=headers, data=json_data)

# Check the response status code
if response.status_code == 200:
    print("Repository updated successfully.")
else:
    print("Failed to update repository. Status code :", response.status_code)
