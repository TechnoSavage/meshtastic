""" weatherBeacon.py v0.2
Retrieve 3 and 6 hour forecasts for a configured location from openweathermap.org and send to a Meshtastic group every hour."""

import argparse
import json
import os
import requests
import time
from datetime import datetime
from getpass import getpass
from meshClass import meshtasticConn

def parseArgs():
    parser = argparse.ArgumentParser(description="Retrieve forecasts for a configured location from openweathermap.org and send to a Meshtastic group at a regular interval.")
    parser.add_argument('-i', '--interval', help='Set the interval, in seconds, at which weather information is retrieved and sent to the mesh. This argument will override the .env file', 
                        type=int, required=False, default=os.environ["INTERVAL"])
    parser.add_argument('-d', '--delay', help='Delay start until local time reaches the nearest half hour', action='store_true', required=False)
    parser.add_argument('--lat', help='Set the location latitude. This argument will override the .env file', 
                        required=False, default=os.environ["LATITUDE"])
    parser.add_argument('--lon', help='Set the location longitude. This argument will override the .env file', 
                        required=False, default=os.environ["LONGITUDE"])
    parser.add_argument('-s', '--service', help='select weather service to retrieve forecast data from', choices=['openweathermap.org'], 
                        required=False, default="openweathermap")
    parser.add_argument('-k', '--key', dest='token', help='Prompt for openweathermap.org API key (do not enter at command line). This argument will override the .env file', 
                        nargs='?', const=None, required=False, default=os.environ["OWM_KEY"])
    parser.add_argument('-p', '--port', help='Set the serial port the Meshtastic radio is connected to. This argument will override the .env file', 
                        required=False, default=os.environ["SERIAL_PORT"])
    parser.add_argument('--version', action='version', version='%(prog)s 0.2')
    return parser.parse_args()

def getForecast(token, lat, lon): 
    """ Get forecast information for supplied lat and lon.

           :param token: A string, openweathermap.org API Key.
           :param lat: A string, latitude of target location.
           :param lon: A string, longitude of target location.
           :returns: A JSON object, forecast data.
           :raises: ConnectionError: if unable to successfully make GET request."""
    
    url = "http://api.openweathermap.org/data/2.5/forecast?"
    payload = {'appid': token,
               'lat': lat,
               'lon': lon,
               'units': 'imperial'}
    try:
        response = requests.get(url, params=payload)
        data = response.content
        return data
    except ConnectionError as error:
        raise error
    
def parseForecast(forecast):
    """ """
    decoded = forecast.decode("utf-8")
    weather = json.loads(decoded)
    nextThree = weather['list'][0]
    nextSix = weather['list'][1]
    print(json.dumps(nextThree, indent=4), json.dumps( nextSix, indent=4))
    return "testing"
    
def main():
    args = parseArgs()
    #conn = meshtasticConn(args.port)
    token = args.token
    if token == None:
        token = getpass(prompt="Enter your API Key: ")
    while True:
        forecast = getForecast(token, args.lat, args.lon)
        conditions = parseForecast(forecast)
        #conn.sendMessage(conditions)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()