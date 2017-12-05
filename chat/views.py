from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

# Django requires CSRF check, this decorator exempts the function from it.
@csrf_exempt
def messages(request):
    # handle request
    # res = handle_request(request)
    data = {
            'messages': [ 
                {
                    'type': 'text', 
                    'text': 'Hello world!'
                }
            ]
            }
    res = JsonResponse(data)
    # Allow CORS access from the UI
    res['Access-Control-Allow-Origin'] = 'http://hipmunk.github.io'
    return res
