"""
Takes date using argprase, check validity then call corresponding weather api
"""
from src.util.weather_helper import Weather_api
import argparse
import datetime
import os
def main():
    '''takes date'''
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help = "Enter date: format should be: YYYY-MM-DD: " ,type = str)
    parser.add_argument("addresses_file_location", nargs='?', default = "src/util/Addresses.json", help = "Give addresses file location", type = str)
    parser.add_argument("output_file_location",  nargs='?', default = "src/util/WeatherData.json", help = "Give Output Directory where weather_information file store", type = str)
    arguments = parser.parse_args()
    '''check valid foramt/date of given date_argument'''
    try:
        datetime.datetime.strptime(arguments.date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    '''call weather_api'''
    Weather_api.weather_information(arguments)

if __name__ == "__main__":
    main()
