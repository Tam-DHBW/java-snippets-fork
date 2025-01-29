import requests

def notify_server(
    server_url: str,
    repository: str,
    ref: str,
    commit: str,
    previous_commit: str,
    pusher: str
):
    """
    Sends a notification to the specified server with repository details.
    """
    # JSON payload to be sentaädsömföäasndfäölknasädlknfälasdknf
    payload = {
        "repository": repository,
        "ref": ref,
        "commit": commit,
        "previous_commit": previous_commit,
        "pusher": pusher,
    }

    try:
        # Send POST request
        response = requests.post(
            server_url,
            json=payload,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(f"Success! Server responded with: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")

if __name__ == "__main__":
    # Example usage
    SERVER_URL = "http://example.com/notify"
    REPOSITORY = "user/repo"
    REF = "refs/heads/main"
    COMMIT = "abcdef1234567890"
    PREVIOUS_COMMIT = "1234567890abcdef"
    PUSHER = "github-user"

    # Call the function
    notify_server(SERVER_URL, REPOSITORY, REF, COMMIT, PREVIOUS_COMMIT, PUSHER)
