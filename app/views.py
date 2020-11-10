from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def snoop(request):
    if request.method == 'POST':
        print('Record_value_via_no_auth: "%s"' % request.body)

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
    if 'Authorization' not in request.headers and request.method == "POST":
        return HttpResponse(status=401)
    elif request.method == "POST":
        token_value = request.headers["Authorization"]
        if not token_value == "yHX1PzQA3n":
            return HttpResponse(status=401)
        else:
            print('Record_value_via_token: "%s"' % request.body)
    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def basic_auth(request):
    print(request.headers)
    return JsonResponse({'client_response': 'ok'})
