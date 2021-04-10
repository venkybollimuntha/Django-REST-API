from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from venkyapp.serializers import NameSerializer

# Create your views here.
class TestAPIView(APIView):

    def get(self,request,*args,**kwargs):
        colors = ['RED',"YELLOW","BLUE"]
        return Response({"msg":"Do festival",'colors':colors},status=200)

    def post(self,request,*args,**kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f"Hello {name}, Happy Pongal"
            return Response({'msg':msg})

        else:
            return Response(serializer.errors, status=400)
    

    def put(self,request,*args,**kwargs):
        return Response({"msg":'This response from put method of APIView'})
    

    def delete(self,request,*args,**kwargs):
        return Response({"msg":'This response from delete method of APIView'})

    def patch(self,request,*args,**kwargs):
        return Response({"msg":'This response from patch method of APIView'})


"""
ViewSet:
--------
list() ---> to get all resources/records
retrieve() --> to get a specific resource
create() --> to create a new resource
update() ---> to perform full updation
partial_update() --> to perform partial update
destroy() ---> to delete a resource.

When ViewSets are Best Choice:
-----------------------------

1. if we want to develop a simple CRUD interface for our database
2. If we want to develop API very quickly
3. If we are performing standard operations
4. If we are not performing any complex operations

ViewSets:

Routers will map views to urls automatically

DRF by default provide DefaultRouter

"""

class TestViewSet(ViewSet):
    def list(self,request):
        colors = ['RED','YELLOW']
        return Response({"msg":"Do festival",'colors':colors},status=200)


    def create(self,request,*args,**kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f"Hello {name}, Happy New Year"
            return Response({'msg':msg})

        else:
            return Response(serializer.errors, status=400)
    


    def retrieve(self,request,pk=None):
        return Response({"msg":'This response from retrieve method of ViewSet'})
    

    def update(self,request,pk=None):
        return Response({"msg":'This response from delete method of ViewSet'})

    def partial_update(self,request,pk=None):
        return Response({"msg":'This response from patch method of ViewSet'})

    def destroy(self,request,pk=None):
        return Response({"msg":'This response from destroy method of ViewSet'})


