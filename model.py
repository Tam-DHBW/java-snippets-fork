import requests
import os

# Server URL (replace with your actual server URL or use an environment variable)
SERVER_URL = os.getenv("SERVER_URL", "http://example.com/notify")

# GitHub event data (replace with actual data or use environment variables)
data = {
    "repository": os.getenv("GITHUB_REPOSITORY", "user/repo"),
    "ref": os.getenv("GITHUB_REF", "refs/heads/main"),
    "commit": os.getenv("GITHUB_SHA", "abcdef1234567890"),
    "previous_commit": os.getenv("GITHUB_EVENT_BEFORE", "1234567890abcdef"),
    "pusher": os.getenv("GITHUB_ACTOR", "github-user")
}

# Send the POST request
try:
    response = requests.post(SERVER_URL, json=data, headers={"Content-Type": "application/json"})
    response.raise_for_status()
    print(f"Success! Server responded with: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
