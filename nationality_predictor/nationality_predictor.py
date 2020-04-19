import requests
import pycountry
import json

def predict(name=""):
    
    if name != "":
        # Requests data from page
        res = requests.get("https://api.nationalize.io/?name={}".format(name))
        status_code = res.status_code
        
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

        if status_code == 422:
            raise ValueError("Invalid name.")
        elif status_code == 200:
            return json.dumps(data, indent=4, ensure_ascii=False)
         
    else:
        raise ValueError("Name is not defined.")