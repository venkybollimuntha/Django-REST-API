from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
	def clean_esal(self): # name must be clean_YOUR_JSON_FIELD_NAME.
		inputsal = self.cleaned_data['esal']
		if inputsal <5000:
			raise forms.ValidationError("the minimum salary must be greater than 5000")
		return inputsal

	class Meta:
		model = Employee
		fields = '__all__'
