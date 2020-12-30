from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.

@csrf_exempt
def get_header(request):
    req_header = dict(request.headers)
    req_header['Url'] = request.scheme + '://' + request.get_host() + request.path
    return JsonResponse(data=req_header)
