import json

from testapp.models import Student

def is_json(data):
	try:
		json.loads(data)
		valid = True
	except ValueError:
		valid = False

	return valid


def get_object_by_id(id):
	try:
		student_data = Student.objects.get(id=id)

	except Student.DoesNotExist:
		student_data = None

	return student_data
