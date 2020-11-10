from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def snoop(request):
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def api_key(request):
    print(request.headers)
    print(request.body)
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def token_auth(request):
    print(request.headers)
    print(request.body)
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})
