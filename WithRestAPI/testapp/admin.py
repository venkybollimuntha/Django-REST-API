from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['eno','ename','esal','eaddr']


# registring your models
admin.site.register(Employee, EmployeeAdmin)