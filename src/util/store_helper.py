"""
data handling
"""
import numpy as np
import json
import requests
class store_helper:
    def get_addresses(self, addresses_file_location):
        '''load addresses from a json file'''
        self.addresses = json.loads(open(addresses_file_location).read())
    @classmethod
    def store_data(cls, keys, data, output_file_location):
        '''store weather data into a json file'''
        with open(output_file_location, 'w') as outfile:
            json.dump(dict(zip(keys, data)), outfile)
