
import requests
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 request.py <sleep_seconds> <node_value>")
        sys.exit(1)
    sleep_seconds = int(sys.argv[1])
    node_value = sys.argv[2]
    time.sleep(sleep_seconds)
    url = "http://dashboard:5000/activate"  # URL del dashboard
    params = {"node": node_value}
    response = requests.get(url, params=params)
    print("Status code:", response.status_code)
    print("Response:", response.text)
    time.sleep(5000)