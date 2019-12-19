from django.http import HttpResponse
from django.core.serializers import serialize
import json

class HttpResponseMixin(object):
    def render_to_http_response(self,data,status_code = 200):
        return HttpResponse(data, content_type = 'appplication/json',status= status_code)


class SerializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json', qs)
        pdict = json.loads(json_data)
        final_list = []
        for p in pdict:
            final_list.append(p['fields'])
        json_data = json.dumps(final_list)
        return json_data

