import requests
import Token

github_token = Token.api_token.Api_token.git_token
# github_token = "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"

# Name and description for the new repository
repo_name = "demo2_re"
repo_description = "This is a new repository created using the GitHub API."

# GitHub API endpoint for creating repositories
create_repo_url = "https://api.github.com/user/repos"

# Data for creating the repository
data = {
    "name": repo_name,
    "description": repo_description,
    "private": False,
    "auto_init": True,
}

# Headers for the request, including authorization and API version
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json",  # API version header
}

# Send a POST request to create the repository
response = requests.post(create_repo_url, json=data, headers=headers)

# Check the response status code
if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
