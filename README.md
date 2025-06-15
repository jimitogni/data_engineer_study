# data_engineer_study

This repository contains utilities and study materials. The project now includes a Python
script for retrieving a bearer token from an HTTP API.

## Getting a bearer token

1. Install the `requests` package if it's not available:

```bash
pip install requests
```

2. Set the following environment variables with your API credentials:

- `API_USERNAME`: your username
- `API_PASSWORD`: your password
- `LOGIN_URL`: (optional) the authentication endpoint. Defaults to
  `https://example.com/api/login`.

3. Run the script:

```bash
python get_bear_token.py
```

The script will print the bearer token to standard output.

