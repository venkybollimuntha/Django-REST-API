from django.shortcuts import render
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework import generics
from rest_framework.pagination import CursorPagination, LimitOffsetPagination, PageNumberPagination
# Create your views here.

class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage' # default value is page
    page_size_query_param = "num"
    max_page_size = 15
    last_page_strings = ('endpage') # default default is last



class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit' # default value is limit
    offset_query_param = "myoffset" # default value is offset
    max_limit = 20


class MyCursorPagination(CursorPagination):
    ordering = '-esal'
    page_size = 5


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # pagination_class = MyCursorPagination
    search_fields = ('^ename','eno',) # No default value # IF you want to include which fields to search add it here
    ordering_fields = ('ename','esal') # default is '__all__' # IF you want to include which fields to order add it here
    # def get_queryset(self):
    #   qs = Employee.objects.all()
    #   name = self.request.GET.get('ename')
    #   if name is not None:
    #       qs = qs.filter(ename__icontains=name)

    #   return qs



