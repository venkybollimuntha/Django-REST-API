from django.shortcuts import render
from django.views.generic import View
from testapp.util import is_json,get_object_by_id
from testapp.mixins import HttpResponseMixin,SerializeMixin
from testapp.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm
import json

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StucentCRUDCBV(HttpResponseMixin,SerializeMixin,View):

    def get(self, request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if valid_json ==False:
            data = json.dumps({'Msg':'Please provide valid json'})
            return self.render_to_http_response(data,status_code=404)
        pdata = json.loads(data)
        print(pdata)
        id = pdata.get('id',None)
        print(id)

        if id:
            student = get_object_by_id(id=id)

            print(student)
            if student is None:
                data = json.dumps({'Msg':'student record not found'})
                return self.render_to_http_response(data, status_code = 404)
            
            json_data = self.serialize([student,])
            return self.render_to_http_response(json_data)

        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if valid_json ==False:
            data = json.dumps({'Msg':'Please provide valid json format'})
            return self.render_to_http_response(data,status_code=400)
        pdata = json.loads(data)

        form = StudentForm(pdata)

        if form.is_valid():
            form.save(commit = True)
            json.dumps({'message':"Record inserted successfully"})
            return self.render_to_http_response(data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status_code = 400)


    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if valid_json ==False:
            data = json.dumps({'Msg':'Please provide valid json format'})
            return self.render_to_http_response(data,status_code=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)

        if id:
            student = get_object_by_id(id=id)
            if student is None:
                data = json.dumps({'Msg':'student record not found'})
                return self.render_to_http_response(data, status_code = 404)
            
            form = StudentForm(pdata,instance=student)
            print(form)

            if form.is_valid():
                form.save(commit = True)
                data = json.dumps({'message':"Record updated successfully"})
                return self.render_to_http_response(data)

            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data,status_code = 400)

        data = json.dumps({'id':'id is mandatory to update'})
        return self.render_to_http_response(data, status_code = 400)


    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if valid_json ==False:
            data = json.dumps({'Msg':'Please provide valid json format'})
            return self.render_to_http_response(data,status_code=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)

        if not id:
            data = json.dumps({'id':'id is must to delete resource'})
            return self.render_to_http_response(data, status_code = 400)

        emp = get_object_by_id(id)
        if not emp:
            data = json.dumps({"message":"The requested resource is not found to delete"})
            return self.render_to_http_response(data, status_code = 400)

        status, deleted_item = emp.delete()

        if status ==1: # status 1 means DB successfully processed the request
            data = json.dumps({"message":"The resource deleted successfully."})
            return self.render_to_http_response(data)

        data = json.dumps({"message":"uanble to delete recored, try again"})
        return self.render_to_http_response(data, status_code = 400)





        






         




