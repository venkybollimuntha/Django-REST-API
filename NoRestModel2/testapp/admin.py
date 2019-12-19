from django.contrib import admin
from testapp.models import Student

# Register your models here.

class StudnetAdmin(admin.ModelAdmin):
	list_display = ['id','name','rollno','marks','gf','bf']


admin.site.register(Student,StudnetAdmin)