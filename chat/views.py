import sys
from . import receive
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, \
                        JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

# Django requires CSRF check, this decorator exempts the function from it.
@csrf_exempt
def messages(request):
    # handle request
    if request.method == 'POST':
        #try:
        response = receive.handle_request(request)
        #except:
        #    print(sys.exc_info()[0])
        #    return HttpResponseBadRequest("Something is wrong with the request")
    else:
        raise Http404("Unsupported HTTP method")
    # Allow CORS access from the UI
    response['Access-Control-Allow-Origin'] = 'http://hipmunk.github.io'
    return response
