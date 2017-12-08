import configparser

from chat import dialog
from chat import actions

from django.http import JsonResponse

def handle_request(request):
    """Given a POST request to /chat/messages, handle the message accordingly"""
    fields = request.POST
    action = fields["action"]
    if action == "join":
        response = received_request_join(fields)
    elif action == "message":
        response = received_request_message(fields)
    else:
        raise ValueError("Unexpected action value \"{}\"".format(action))

    return response

def handle_DM_response(response):
    """
    Handles the response of the dialog manager. The response could be a 
    command to perform futher actions, or it could be a message to be sent 
    to the user.
    """
    if response.get_type() == "text":
        return str(response)
    elif response.get_type() == "command":
        return handle_command(response.get_command_type(), 
                              response.get_params())
    else:
        raise ValueError("Unknown type of response from dialog manager: \"{}\""\
                                                   .format(response.get_type()))

def received_request_join(fields):
    response = handle_DM_response(dialog.handle_event("join", fields))
    return compose_response(response)

def received_request_message(fields):
    response = handle_DM_response(dialog.handle_message(fields["text"]))
    return compose_response(response)

def handle_command(command, params):
    """
    Given a command from the dialog manager, and some parameters. Perform 
    the corresponding actions, then return a message response to be sent to 
    the user.
    """
    if command == "get-weather":
        response = actions.get_weather(params["location"])
    else:
        raise ValueError("Unknown command from dialog manager: \"{}\""\
                                                               .format(command))
    return response
    
def compose_response(message):
    response_data = {
               'messages': [ 
                   {
                       'type': 'text', 
                       'text': message
                   }
               ]
            }
    return JsonResponse(response_data)

