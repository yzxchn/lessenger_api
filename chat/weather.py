import configparser, json
from urllib import request, parse

config = configparser.ConfigParser()
config.read_file(open('keys.config'))

GMAPS_KEY = config["GMAPS"]["access_token"]
DARKSKY_KEY = config["DARKSKY"]["access_token"]

def get_coordinates(location):
    """
    For a given location string, find an exact coordinate using Google Maps API.
    """
    params = parse.urlencode({"address": location, "key": GMAPS_KEY})
    url = "https://maps.googleapis.com/maps/api/geocode/json?{}".format(params)
    results = json.load(request.urlopen(url))["results"]
    if results:
        coordinates = results[0]["geometry"]["location"]
    else:
        coordinates = None
    return coordinates

def get_darksky_weather(location):
    """
    Given a location string, find the current weather at that location, using 
    DarkSky API.
    """
    coordinates = get_coordinates(location)
    if coordinates:
        lng = coordinates["lng"]
        lat = coordinates["lat"]
    else:
        raise LocationNotFoundError("Can not find location: {}".format(location))

    url = "https://api.darksky.net/forecast/{}/{},{}".format(DARKSKY_KEY, 
                                                             lat, lng)
    result = json.load(request.urlopen(url))
    try:
        summary = result["currently"]["summary"]
        temperature = result["currently"]["temperature"]
    except KeyError:
        raise WeatherNotFoundError
    
    return summary, temperature

class Error(Exception):
    pass

class LocationNotFoundError(Error):
    pass

class WeatherNotFoundError(Error):
    pass
    

if __name__ == "__main__":
    print(get_darksky_weather("San Francisco"))
    
