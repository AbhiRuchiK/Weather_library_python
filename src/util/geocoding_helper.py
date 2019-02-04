"""Call mapbox api for getting coordinates"""
import numpy as np
import requests
class geocoder_helper():
    @classmethod
    def get_coordinates(cls, addresses):
        '''map addresses with url to get geo coordinates'''
        addresses_url = np.array([ "https://api.mapbox.com/geocoding/v5/mapbox.places/"
                                  + addresses[key]
                                  +".json?access_token=pk.eyJ1IjoiYmprcCIsImEiOiJjanJreW5ib3UwMnB6NDNvOW9tOGJjZjIxIn0.S9pzxs5l-G9ELuU1QXpVig"
                                  for key in addresses.keys()])
        return ([*map(lambda geo_data : str(geo_data['features'][1]['center'][1])+","+str(geo_data['features'][1]['center'][0]) , ([*map(lambda url : requests.get(url).json(), addresses_url)]))])
