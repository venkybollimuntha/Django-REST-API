from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializers
# Create your views here.

# class must be child class of the rest_framwork ModelViewSet
class EmployeeCRUDCBV(ModelViewSet):
	queryset = Employee.objects.all()

	serializer_class = EmployeeSerializers

	# still continue

