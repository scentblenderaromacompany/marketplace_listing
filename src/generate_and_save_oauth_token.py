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
    client_id = "RobertCa-EEEListi-SBX-473448ebb-3cf6b0b0"
    client_secret = "SBX-73448ebbef34-3dd8-40bd-816d-3ef3"
    token_response = generate_oauth_token(client_id, client_secret)
    access_token = token_response['access_token']
    
    # Save the token to a file
    with open('oauth_token.txt', 'w') as token_file:
        token_file.write(access_token)
    
    print("OAuth token saved to oauth_token.txt")
