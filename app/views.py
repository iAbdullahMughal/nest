from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

TOKEN_AUTH = "Bearer yHX1PzQA3n"


@csrf_exempt
def snoop(request):
    if request.method == 'POST':
        print('Raw Data - No auth: "%s"' % json.dumps(request.body.decode("utf8"), indent=2))

    return JsonResponse({'client_response': 'ok'})


@csrf_exempt
def api_key(request):
    print("==============================")
    print(request.headers)
    print(request.method)
    print(request.body)
    print("==============================")
    if request.method == 'POST':
        print('Raw Data -- api key: "%s"' % request.body)

    return JsonResponse({'client_response': 'ok'})


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
    print("==============================")
    print(request.headers)
    print(request.method)
    print(request.body)
    print("==============================")
    return JsonResponse({'client_response': 'ok'})
