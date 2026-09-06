#Endooint set up.
import requests

#v3 API link is out of service, documentation provided v5.
url = "https://api.restcountries.com/countries/v5"

#To facilitate pulling desired fields from json dataset.
desired_fields = {"response_fields": "names.common, capitals, region, population"}

#header used as per v5 api documentation; v3 version OOO.
headers= {'Authorization': 'Bearer rc_live_985b1ecf76044c8da5f1009876fad3c9'}
response = requests.get(url, 
                        headers= headers,
                        params= desired_fields)

data = response.json()

#Set up list to append target fields via loop.
country_list = []

#data, objects are first layers in json dataset prior to accessing descired fields.
for things in data['data']['objects']:
    country_list.append({
        "name": things['names']['common'],
        "capital": things['capitals'][0]['name'] if things.get("capitals") else "N/A",
        "region": things["region"],
        "population": things["population"]
    })

#Menu set up on basis of while loop; option var to capture input and loop set up.
option = 0
while option != 3:
    print(f" === Country Explorer === ")
    print(f" 1. Search by name ")
    print(f" 2. Filter by region ")
    print(f" 3. quit")

 # try/except for exception capture during assessment of data entry/input.
    try:
        option = int(input("Choose an option (1-3):")) 
        if option == 1:
            search_term = input(f"Enter a search term:")
            for item in country_list:

                #To capture country that corresponds with search term. force case and use of 'in'
                if search_term.lower() in item['name'].lower():
                    print(f"{item['name']} - Capital: {item['capital']} | Region: {item['region']} | Population: {item['population']:,}")
        elif option == 2:
            region_input = input(f"Enter a region to search by:")

            #Pulling population, country name so as to sort first, then output name.
            regions = []
            for item in country_list:
                if region_input.lower() in item['region'].lower():
                    regions.append([item['population'], item['name']])

            #use of sort, reverse - t to sort by population. 
            sorted_region = sorted(regions, reverse= True)
            for name in sorted_region:
                print(name[1])
        #To capture odd instances of data entry. Ths is meant to capture correct data type
        #but incorrect input
        elif option < 1 or option > 3:
            print(f"Invalid. Choose an available option.")
    #below, meant to capture incorrect data type data entry. 
    except ValueError:
        print(f"Please insert only one of the available options.")

    
