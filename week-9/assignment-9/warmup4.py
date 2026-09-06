#Endpoint set up.
import requests

url = "https://thisurldoesnotexist.example.com"

#try/except exception handling, checking status code = 200 prior to pulling json data.
try:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: An HTTP error occurred.")
    else:
        data = response.json()
except requests.exceptions.RequestException:
    print(f"Error: Could not reach the server. Check your connection and try again.")

