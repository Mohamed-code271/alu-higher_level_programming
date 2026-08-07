# python-network_1

Python scripts using `urllib` and `requests` to send HTTP requests, handle headers, POST data, JSON responses, and error codes.

## Files

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches the ALU intranet status page using `urllib` |
| `1-hbtn_header.py` | Displays the `X-Request-Id` header value using `urllib` |
| `2-post_email.py` | Sends a POST request with an `email` param using `urllib` |
| `3-error_code.py` | Displays the response body, or the HTTP error code, using `urllib` |
| `4-hbtn_status.py` | Fetches the ALU intranet status page using `requests` |
| `5-hbtn_header.py` | Displays the `X-Request-Id` header value using `requests` |
| `6-post_email.py` | Sends a POST request with an `email` param using `requests` |
| `7-error_code.py` | Displays the response body, or the error code (>= 400), using `requests` |
| `8-json_api.py` | Sends a POST request with a letter and displays JSON search results |
| `10-my_github.py` | Displays a GitHub user's id using Basic Authentication |

## Usage

```bash
./0-hbtn_status.py
./1-hbtn_header.py <url>
./2-post_email.py <url> <email>
./3-error_code.py <url>
./4-hbtn_status.py
./5-hbtn_header.py <url>
./6-post_email.py <url> <email>
./7-error_code.py <url>
./8-json_api.py <letter>
./10-my_github.py <username> <token>
```
