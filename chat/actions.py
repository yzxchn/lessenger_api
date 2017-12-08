import chat.dialog as dialog
import chat.weather as wt

from . import receive as rv

def get_weather(location):
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
