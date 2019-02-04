import json
import numpy as np
import requests
from store_helper import store_helper
import pytest

def test_get_addresses():
    addresses = json.loads(open('src/util/Addresses.json').read())
    assert addresses == {'0': 'Pratap Nagar', '1': 'Jaipur', '2': 'Delhi', '3': 'Udaipur', '4': 'Ajmer', '5': 'Gurugram', '6': 'Pune', '7': 'Mumbai', '8': 'Ahmedabad'}

def test_store_data():
    addresses = json.loads(open('src/util/Addresses.json').read())
    addresses_url = np.array([ "https://api.mapbox.com/geocoding/v5/mapbox.places/"
                              + addresses[key]
                              +".json?access_token=pk.eyJ1IjoiYmprcCIsImEiOiJjanI3YXh1MzYwaGgxNDNuajZvejJ3a252In0.jFYwf5KFBFym5Itx_GDA5A"
                              for key in addresses.keys()])
    data = ([*map(lambda geo_data : str(geo_data['features'][1]['center'][1])+","+str(geo_data['features'][1]['center'][0]) , ([*map(lambda url : requests.get(url).json(), addresses_url)]))])
    assert (store_helper.store_data(addresses.values(), data,  'src/util/test_store_weather_data.json')) == None
