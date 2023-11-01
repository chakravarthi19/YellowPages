import requests

# r = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
r = requests.get("https://reqres.in/api/users?page=2")


email = "eve.holt@reqres.in"
password = "pistol"

# Create a dictionary containing the email and password for basic authentication
headers = {
    "Authorization": f"Basic {email}:{password}"
}

# Send a GET request with the headers
response = requests.get('https://reqres.in/api/register', headers=headers)

# user_creation = requests.post('https://reqres.in/api/register', headers=headers)
# Check the response
if response.status_code == 200:
    print("Request was successful.")
    data = response.json()  # If the response is JSON
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
