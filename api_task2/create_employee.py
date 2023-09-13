import requests

# Define the API endpoint URL where you want to create employees
api_url = 'https://example.com/api/employees'  # Replace with your actual API endpoint

# Replace with your actual authentication token or API key if required
headers = {
    'Authorization': 'Bearer YOUR_API_TOKEN',
    'Content-Type': 'application/json'
}

# Create employee data for 10 employees
for i in range(1, 11):
    employee_data = {
        'name': f'Employee {i}',
        'age': 25 + i,
        'designation': 'Associate'
    }

    # Send a POST request to create the employee
    response = requests.post(api_url, json=employee_data, headers=headers)

    if response.status_code == 201:
        print(f"Employee {i} created successfully.")
    else:
        print(f"Failed to create Employee {i}. Status code: {response.status_code}")

# Note: In this example, you need to replace 'https://example.com/api/employees' with the actual API endpoint where you want to create employees.
