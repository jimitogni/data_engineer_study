import os
import requests

def get_token(login_url: str, username: str, password: str) -> str:
    """Obtain a bearer token from an HTTP API."""
    response = requests.post(
        login_url,
        data={"username": username, "password": password},
        headers={"Accept": "application/json"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    token = data.get("token") or data.get("access_token")
    if not token:
        raise ValueError("Token not found in response")
    return token


def main() -> None:
    login_url = os.environ.get("LOGIN_URL", "https://example.com/api/login")
    username = os.environ["API_USERNAME"]
    password = os.environ["API_PASSWORD"]

    token = get_token(login_url, username, password)
    print(token)


if __name__ == "__main__":
    main()
