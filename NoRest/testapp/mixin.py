from django.http import HttpResponse

class HttpResponseMixin(object):
	def render_http_to_response(self,json_data):
		return HttpResponse(json_data,content_type='application/json')