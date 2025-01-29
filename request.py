import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Success!")
    print("Response content:", response.json())
else:
    print("Request failed with status:", response.status_code)
