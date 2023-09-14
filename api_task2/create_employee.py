import base64
import requests
import json

# GitHub repository information
repo_owner = 'Ashwanirawat1'
repo_name = 'Api_terra'
file_path = 'api_task2/employeejso.json'

# Set the GitHub API endpoint URL for the specific file in the repository
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

# GitHub personal access token
github_token = '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'

# Content of the new file
file_content = '''[
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


# Encode the file content to base64
content_base64 = base64.b64encode(file_content.encode()).decode()

# Payload for creating the new file
payload = {
    "message": "Create new file",
    "content": content_base64,
    "branch": "main"
}

# Headers for the request
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Send a PUT request to create the new file
response = requests.put(url, json=payload, headers=headers)

if response.status_code == 201:
    print("File created successfully!")
else:
    print(f"Failed to create file. Status code: {response.status_code}")
