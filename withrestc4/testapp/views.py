from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,
DjangoModelPermissions,
DjangoModelPermissionsOrAnonReadOnly,)

from testapp.permissions import IsReadOnly,IsGETOrPatch
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from authentications import CustomAuthentication
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	authentication_classes= [CustomAuthentication,]
	permission_classes = [IsAuthenticated,]


