# python-network_0

Bash scripts using `curl` to interact with a web server, covering request bodies, methods, headers, and POST parameters.

## Files

| File | Description |
| --- | --- |
| `0-body_size.sh` | Sends a request to a URL and displays the size of the response body, in bytes |
| `1-body.sh` | Sends a GET request and displays the response body, only if the status code is 200 |
| `2-delete.sh` | Sends a DELETE request to a URL and displays the response body |
| `3-methods.sh` | Sends an OPTIONS request and displays all HTTP methods the server accepts |
| `4-header.sh` | Sends a GET request with the header `X-HolbertonSchool-User-Id: 98` and displays the response body |
| `5-post_params.sh` | Sends a POST request with `email` and `subject` parameters and displays the response body |

## Usage

```bash
./0-body_size.sh <url>
./1-body.sh <url>
./2-delete.sh <url>
./3-methods.sh <url>
./4-header.sh <url>
./5-post_params.sh <url>
```
