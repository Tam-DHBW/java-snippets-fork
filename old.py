import os
import requests

def notify_server():
    """
    Sends a notification to the server with repository details from environment variables.
    """
    # Load configuration from environment variables
    server_url = os.getenv("SERVER_URL", "http://example.com/notify")
    repository = os.getenv("REPOSITORY", "user/repo")
    ref = os.getenv("REF", "refs/heads/main")
    commit = os.getenv("COMMIT", "abcdef1234567890")
    previous_commit = os.getenv("PREVIOUS_COMMIT", "1234567890abcdef")
    pusher = os.getenv("PUSHER", "github-user")

    # Prepare the JSON payload
    payload = {
        "repository": repository,
        "ref": ref,
        "commit": commit,
        "previous_commit": previous_commit,
        "pusher": pusher,
    }

    try:
        # Send the POST request
        response = requests.post(
            server_url,
            json=payload,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Notification sent successfully! Server response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    notify_server()
