from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def emp_data_view(request):
	emp_data = {
	'eno':100,
	'ename': 'sunny',
	"esal": 1000,
	}
	return HttpResponse(emp_data)


def emp_json_data_view(request):
	emp_data = {
	'eno':100,
	'ename': 'sunny',
	"esal": 1000,
	}
	resp = json.dumps(emp_data)
	return HttpResponse(resp)

from django.http import JsonResponse
def emp_json_data_view2(request):
	emp_data = {
	'eno':100,
	'ename': 'sunny',
	"esal": 1000,
	}
	return JsonResponse(emp_data)

# class based view
from django.views.generic import View
from testapp.mixin import HttpResponseMixin

class JsonCBV(HttpResponseMixin,View):
	def get(self, request,*args,**kwargs):
		emp_data = {
		'eno':100,
		'ename': 'sunny',
		"esal": 1000,
		}
		return self.render_http_to_response(emp_data)

