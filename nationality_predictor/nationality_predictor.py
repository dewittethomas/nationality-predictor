import requests
import pycountry
import json

def predict(name=""):
    
    if name != "":
        # Requests data from page
        res = requests.get("https://api.nationalize.io/?name={}".format(name))
        
        name = res.json()["name"]
        countries = res.json()["country"]

        if len(countries) != 0:
            # Converts ISO-code to country name
            for country in countries:
                code = country["country_id"]
                del country["country_id"]

                country_name = pycountry.countries.get(alpha_2=code).name
                country["country_name"] = country_name

                probability = country["probability"]
                del country["probability"]
                country["probability"] = probability

        else:
            countries = []
        
        # Returns json of data
        data = {
            'name': name,
            'countries': countries
        }

        data = json.dumps(data, indent=4, ensure_ascii=False)

        return data
        
    else:
        raise ValueError("Missing 'name' parameter.")