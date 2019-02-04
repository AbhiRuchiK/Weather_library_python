from geocoding_helper import geocoder_helper
import json
def test_geocoder_helper():
    addresses = json.loads(open('src/util/Addresses.json').read())
    geo_coordinates_result = geocoder_helper.get_coordinates(addresses)
    assert geo_coordinates_result == ['26.777496,75.912384', '26.82803,75.80581', '37.36901,97.36008', '24.619894,73.890396', '26.917595,75.817184', '28.46169,77.08146', '18.328915,73.993103', '19.05,72.83333', '23.03,72.58']
