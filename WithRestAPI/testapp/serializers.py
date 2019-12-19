from testapp.models import Employee
from rest_framework.serializers import ModelSerializer

class EmployeeSerializers(ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


