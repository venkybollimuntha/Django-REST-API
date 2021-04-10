# eg1:

# I need to create a permission class 
# that allows only SAFE Methods

from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsReadOnly(BasePermission):
	def has_permission(self,request,view):
		if request.method in SAFE_METHODS:
			return True
		return False

class IsGETOrPatch(BasePermission):
	def has_permission(self,request,view):
		allowed_methods = ['GET','PATCH']
		if reqeust.method in allowed_methods:
			return True

		return False