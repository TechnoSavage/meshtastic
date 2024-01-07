
import json
import os
import requests
import time
from meshClass import meshtasticConn

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
               'units': 'standard'}
    try:
        response = requests.get(url, params=payload)
        data = response.content
        return data
    except ConnectionError as error:
        raise error
    
def parseForecast(forecast):
    """ """
    weather = forecast.decode("utf-8")
    loaded = json.loads(weather)
    print(json.dumps(loaded, indent=4))
    return "testing"
    
def main():
    port = os.environ["SERIAL_PORT"]
    conn = meshtasticConn(port)
    token = os.environ["OWM_KEY"]
    lat = os.environ["LATITUDE"]
    lon = os.environ["LONGITUDE"]
    while True:
        forecast = getForecast(token, lat, lon)
        conditions = parseForecast(forecast)
        conn.sendMessage(conditions)
        time.sleep(3600)

if __name__ == "__main__":
    main()