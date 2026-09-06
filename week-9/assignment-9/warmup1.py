import requests

response = requests.get("https://api.agify.io/?name=michael")
json_data = response.json()
reordered_json = json_data.pop("count")
json_data["count"] = reordered_json
print(f"Status code: {response.status_code}")
print(f"Response: {json_data}")