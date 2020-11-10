from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

TOKEN_AUTH = "Bearer yHX1PzQA3n"


@csrf_exempt
def snoop(request):
    print(json.dumps(request.headers))
    print(request.method)
    if request.method == 'POST':
        print('Record_value_via_no_auth: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def api_key(request):
    print(json.dumps(request.headers))
    print(request.method)
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def token_auth(request):
    print("=================================")
    print(request.method)
    print(request.headers)
    print(request.body)
    print("=================================")
    if request.method == "POST":
        pass
    elif request.method == "GET":
        if 'Authorization' in request.headers:
            __token_auth__ = request.headers["Authorization"]
            if __token_auth__ == TOKEN_AUTH:
                return JsonResponse({'client_response': 'ok'})
            else:
                # Failed to match Token ID
                return HttpResponse(status=401)
        else:
            # Failed to get Token ID
            return HttpResponse(status=401)


@csrf_exempt
def basic_auth(request):
    print(request.headers)
    return JsonResponse({'client_response': 'ok'})
