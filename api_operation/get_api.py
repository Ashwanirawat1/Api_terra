import requests

token = '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'

url = 'https://api.github.com/user/repos'

# Define the headers with the token
headers = {
    'Authorization': f'token {token}',
}

# Send a GET request to retrieve the list of repositories
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    repos = response.json()
    # Extract and print the repository names
    repo_names = [repo['name'] for repo in repos]
    for name in repo_names:
        print(name)
else:
    print("Failed to retrieve repositories. Status code:", response.status_code)
