from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

TOKEN_AUTH = "Bearer yHX1PzQA3n"


@csrf_exempt
def snoop(request):
    if request.method == 'POST':
        print('Raw Data - No auth: "%s"' % request.body.decode("utf8"))

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def api_key(request):
    if request.method == 'POST':
        if "Encryption-Key" in request.headers:
            encryption_key = request.headers["Encryption-Key"]
            if encryption_key == "kTZEIDEV7gHXTh7b3JHonpDCvi3vjTmd":
                print('Raw Data -- api key: "%s"' % request.body)

                return JsonResponse({'client_response': 'ok'})
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=403)
    elif request.method == "GET":
        return HttpResponse(status=403)


@csrf_exempt
def token_auth(request):
    if request.method == "POST":
        print('Raw Data - token auth: "%s"' % request.body)
    elif request.method == "GET":
        if 'Authorization' in request.headers:
            __token_auth__ = request.headers["Authorization"]
            if __token_auth__ == TOKEN_AUTH:
                return JsonResponse({'client_response': 'ok'})
            else:
                # Failed to match Token ID
                return HttpResponse(status=403)
        else:
            # Failed to get Token ID
            return HttpResponse(status=403)


@csrf_exempt
def basic_auth(request):
    print(request.headers)
    print(request.body)
    if request.method == "POST":
        print('Raw Data - basic auth: "%s"' % request.body)
    elif request.method == "GET":
        print(request.headers)
        print(request.body)
    return JsonResponse({'client_response': 'ok'})
