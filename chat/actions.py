import chat.dialog as dialog
import chat.weather as wt

from . import receive as rv

def get_weather(location):
    """This action should be called when the dialog manager sends the 
    "get-weather" command. It takes a location string, and finds the weather 
    information for that location. Then talks to dialog manager to compose a 
    message incorporating the weather information.

    Args:
        location (str): a string representing an address or zip code. 

    Returns: 
        str: a message describing the weather information. (e.g. "Currently, 
             it's 59F. Cloudy.")
    """
    try:
        summary, temp = wt.get_darksky_weather(location)
        params = {"summary": summary, "temperature": temp}
        dm_response = dialog.handle_event("report-weather", params)
        response = rv.handle_DM_response(dm_response)
    except wt.LocationNotFoundError:
        dm_response = dialog.handle_event("loc-not-found", {})
        response = rv.handle_DM_response(dm_response)
    except wt.WeatherNotFoundError:
        dm_response = dialog.handle_event("weather-not-found", {})
        response = rv.handle_DM_response(dm_response)

    return response
