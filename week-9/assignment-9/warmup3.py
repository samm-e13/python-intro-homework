import requests
url = "https://api.restcountries.com/countries/v5"
desired_fields = {"region": "Europe", "response_fields": "names.common"}
headers= {'Authorization': 'Bearer rc_live_985b1ecf76044c8da5f1009876fad3c9'}
response = requests.get(url, 
                        headers= headers,
                        params= desired_fields)

data = response.json()
counter = 1
for things in data['data']['objects']:
    if counter > 10:
        break
    else:
        data_list = things['names']['common']
        print(data_list)
        counter +=1



