from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from testapp.mixin import SerializeMixin,ReturnResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import EmployeeForm
from testapp.utils import is_json, get_user_by_id
import json
# Create your views here.
@method_decorator(csrf_exempt, name = 'dispatch')
class EmployeeDetailCBV(ReturnResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            data = json.dumps({"message":"The requested resource is not found."})
            return self.returnResponse(data,status_code=404)
        else:
            data = self.serialize([emp])
            return self.returnResponse(data)

    def put(self,request,id,*args,**kwargs):
        orignal_data = get_user_by_id(id)
        if not orignal_data:
            data = json.dumps({"message":"The requested resource is not found to update"})
            return self.returnResponse(data,status_code=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
           return  self.returnResponse({'Message':"Please send valid json data"},status_code=400)

        given_data = json.loads(data)

        form = EmployeeForm(given_data,instance=orignal_data) # Here instance is important to updata data otherwise data is inserted.
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource updated successfully'})
            return self.returnResponse(json_data,status_code=200)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.returnResponse(json_data, status_code=400)


    def delete(self,request,id, *args, **kwargs):
        emp = get_user_by_id(id)
        if not emp:
            data = json.dumps({"message":"The requested resource is not found to delete"})
            return self.returnResponse(data,status_code=404)

        status, deleted_item = emp.delete()

        if status ==1: # status 1 means DB successfully processed the request
            data = json.dumps({"message":"The resource deleted successfully."})
            return self.returnResponse(data,status_code=200)

        data = json.dumps({"message":"uanble to delete recored, try again"})
        return self.returnResponse(data,status_code=400)


@method_decorator(csrf_exempt, name = 'dispatch')
class EmployeeListDetailCBV(ReturnResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            emp = Employee.objects.all()  
        except Employee.DoesNotExist:
            data = json.dumps({"message":"The requested resource is not found."})
            return self.returnResponse(data,status_code=404)
        else:
            data = self.serialize(emp)
            return self.returnResponse(data,status_code=200)


    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
           return  self.returnResponse({'Message':"Please send valid json data"},status_code=400)
        
        empdata = json.loads(data)
        # to save form data of post request you must have forms in django so create a forms.py file and extend models in that.
        form = EmployeeForm(empdata)
        
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource created successfully'})
            return self.returnResponse(json_data,status_code=200)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.returnResponse(json_data, status_code=400)

    
