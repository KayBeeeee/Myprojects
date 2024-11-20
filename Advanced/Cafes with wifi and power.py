#This project using API's
# To get and list cafes with wifi and power for remote working
# To get and list cafes with wifi and power for remote working
import requests
import json
from pprint import pprint

def get_cafe():
    url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX<YOUR_GoogleAPIKey_HERE>"
    response = requests.get(url)
    data = response.json()
    results = data['results']
    for result in results:
        name = result['name']
        rating = result['rating']
        if 'price_level' in result:
            price_level = result['price_level']
        else:
            price_level = 'No data'
        if 'opening_hours' in result and result['opening_hours']['open_now']:
            open_now = 'Open'
        else:
            open_now = 'Close'
        if 'business_status' in result:
            business_status = result['business_status']
        else:
            business_status = 'No data'
        print(f"Name: {name}\nRating: {rating}\nPrice Level: {price_level}\nOpen Now: {open_now}\nBusiness Status: {business_status}\n")

get_cafe()

