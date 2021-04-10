from django.shortcuts import render

from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,ListAPIView, CreateAPIView
# Create your views here.

# class EmployeeListAPIView(APIView):
# 	def get(self, request, *args,**kwargs):

# 		qs = Employee.objects.all()
# 		serializers = EmployeeSerializer(qs,many=True)
# 		return Response(serializers.data)

# class EmployeeListAPIView(ListAPIView):
# 	# queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer 
# 	def get_queryset(self):
# 		qs = Employee.objects.all()
# 		name = self.request.GET.get('ename')
# 		if name is not None:
# 			qs = qs.filter(ename__icontains=name)

# 		return qs


# class EmployeeCreateAPIView(CreateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer


# class EmployeeRetrieveAPIView(RetrieveAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	# lookup_field = 'id' # if you want to use your own variable name
# 	# by default it will be pk.

# from rest_framework.generics import UpdateAPIView

# class EmployeeUpdateAPIView(UpdateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# from rest_framework.generics import DestroyAPIView
# class EmployeeDestroyAPIView(DestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# from rest_framework.generics import ListCreateAPIView
# class EmployeeListCreateAPIView(ListCreateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# from rest_framework.generics import RetrieveUpdateAPIView
# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer



# from rest_framework.generics import RetrieveDestroyAPIView
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer


# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer



from rest_framework import mixins,generics
class EmployeeListCreateModelMixin(mixins.CreateModelMixin,generics.ListAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def post(self,request,*args,**kwargs):
		return self.create(request, *args, **kwargs)


class EmployeeRetrieveUpdateDestroyModelMixin(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.partial_update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.delete(request,*args,**kwargs)
		



