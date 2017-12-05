from django.http import JsonResponse

def handle_request(request):
    """Given a POST request to /chat/messages, handle the message accordingly"""
    fields = request.POST
    action = fields["action"]
    if action == "join":
        response = handle_join(fields)
    elif action == "message":
        response = handle_message(fields)
    else:
        raise ValueError("Unexpected action value \"{}\"".format(action))

    return response

def handle_join(fields):
    response_data = {
               'messages': [ 
                   {
                       'type': 'text', 
                       'text': 'Hello, {}!'.format(fields["name"])
                   }
               ]
            }
    return JsonResponse(response_data)

def handle_message(fields):
    pass

