import requests

url = "https://thisurldoesnotexist.example.com"

try:
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print(f"Error: An HTTP error occurred.")
except requests.exceptions.RequestException:
    print(f"Error: Could not reach the server. Check your connection and try again.")

