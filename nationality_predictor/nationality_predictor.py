import requests, pycountry, json

def predict(name=""):
    if name != "":
        url = "name={}".format(name)

        req = requests.get("https://api.nationalize.io?{}".format(url))
        status_code = req.status_code
        result = json.loads(req.text)

        countries = result["country"]
        
        if countries != []:
            for country in countries:
                country["country_id"] = pycountry.countries.get(alpha_2=country["country_id"]).name
                country["country_name"] = country.pop("country_id") 

            data = {
                'name': result['name'],
                'countries': result['country']
            }

        if status_code == 422:
            raise ValueError("Invalid name.")
        elif status_code == 200:
            return json.dumps(data, indent=4, ensure_ascii=False)
                
    else:
        raise ValueError("Name is not defined.")