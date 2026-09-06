import requests

url = "https://thisurldoesnotexist.example.com"

try:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: An HTTP error occurred.")
    else:
        data = response.json()
except requests.exceptions.RequestException:
    print(f"Error: Could not reach the server. Check your connection and try again.")

