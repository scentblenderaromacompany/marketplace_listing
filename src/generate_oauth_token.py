import requests

def generate_oauth_token(client_id, client_secret):
    url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    token_response = generate_oauth_token(client_id, client_secret)
    with open('oauth_token.txt', 'w') as token_file:
        token_file.write(token_response['access_token'])
    print(token_response)
