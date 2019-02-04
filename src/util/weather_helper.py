import requests
import json
import datetime
import pandas as pd
import numpy as np
from src.util.store_helper import store_helper
from src.util.geocoding_helper import geocoder_helper

class Weather_api():
    @classmethod
    def weather_information(cls, argparse_arguments):
        '''takes addresses from json file '''
        addresses_dto = store_helper()
        addresses_dto.get_addresses(argparse_arguments.addresses_file_location)
        '''get coordinates(latitude, longitude) of addresses'''
        geo_coordinates = geocoder_helper.get_coordinates(addresses_dto.addresses)
        '''gathering weather data from darksky api using geo_coordinates'''
        weather_dto = [*map(lambda x :  requests.get('https://api.darksky.net/forecast/5a5c8edbd9f058b6120fda0b4064edbc/'
                                              + x + "," + argparse_arguments.date + 'T00:00:00').json(), geo_coordinates)]
        '''store data in a json file'''
        store_helper.store_data(addresses_dto.addresses.values(), weather_dto, argparse_arguments.output_file_location)
