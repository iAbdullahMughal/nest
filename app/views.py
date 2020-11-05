from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def snoop(request):
    #
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)


    return JsonResponse({'client_response': 'ok'})
