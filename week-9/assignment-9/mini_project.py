import requests

url = "https://api.restcountries.com/countries/v5"
desired_fields = {"response_fields": "names.common, capitals, region, population"}
headers= {'Authorization': 'Bearer rc_live_985b1ecf76044c8da5f1009876fad3c9'}
response = requests.get(url, 
                        headers= headers,
                        params= desired_fields)

data = response.json()
country_list = []
for things in data['data']['objects']:
    country_list.append({
        "name": things['names']['common'],
        "capital": things['capitals'][0]['name'] if things.get("capitals") else "N/A",
        "region": things["region"],
        "population": things["population"]
    })

option = 0
while option != 3:
    print(f" === Country Explorer === ")
    print(f" 1. Search by name ")
    print(f" 2. Filter by region ")
    print(f" 3. quit")

    try:
        option = int(input("Choose an option (1-3):")) 
        if option == 1:
            search_term = input(f"Enter a search term:")
            for item in country_list:
                if search_term.lower() in item['name'].lower():
                    print(f"{item['name']} - Capital: {item['capital']} | Region: {item['region']} | Population: {item['population']:,}")
        elif option == 2:
            region_input = input(f"Enter a region to search by:")
            regions = []
            for item in country_list:
                if region_input.lower() in item['region'].lower():
                    regions.append([item['population'], item['name']])
            sorted_region = sorted(regions, reverse= True)
            for name in sorted_region:
                print(name[1])
        elif option < 1 or option > 3:
            print(f"Invalid. Choose an available option.")
        
    except ValueError:
        print(f"Please insert only one of the available options.")

    
