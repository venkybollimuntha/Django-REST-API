from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
	def marks(self):
		inputsal = self.cleaned_data['marks']
		if inputsal <35:
			raise forms.ValidationError("Marks must be less than 35uu")
		return inputsal

	class Meta:
		model = Student
		fields = '__all__'
