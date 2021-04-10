from django.shortcuts import render
import requests
# Create your views here.

def get_geographic_info(request):
	ip = request.META.get('HTTP_X_FORWARDED_FOR','') or request.META.get('REMOTE_ADDR')
    url = ''

    # here you have to send request to Ipstack endpoint.

    