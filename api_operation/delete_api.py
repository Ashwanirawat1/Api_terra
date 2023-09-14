import requests

token = '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'

# Set the GitHub repository URL
repo_owner = 'Ashwanirawat1'
repo_name = 'demo2_re'

# Set the GitHub API endpoint URL for the specific repository
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

# Define the headers with the token
headers = {
    'Authorization': f'token {token}',
}

# Send a DELETE request to delete the repository
response = requests.delete(url, headers=headers)

# Check the response status code
if response.status_code == 204:
    print("Repository deleted successfully")
else:
    print("Failed to delete repository. Status code:", response.status_code)
