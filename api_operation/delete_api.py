import requests
import Token

# github_token = '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'
github_token = Token.api_token.Api_token.git_token
# Set the GitHub repository URL
repo_owner = 'Ashwanirawat1'
repo_name = 'demo2_re'

# Set the GitHub API endpoint URL for the specific repository
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

# Define the headers with the token
headers = {
    'Authorization': f'token {github_token}',
}

# Send a DELETE request to delete the repository
response = requests.delete(url, headers=headers)

# Check the response status code
if response.status_code == 204:
    print("Repository deleted successfully")
else:
    print("Failed to delete repository. Status code:", response.status_code)
