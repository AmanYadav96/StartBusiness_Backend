
from rest_framework.permissions import BasePermission,SAFE_METHODS

# 

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_role.lower() == "manager"

#  Admin Permission 
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role.lower()=='admin'
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role.lower()=='customer'
    
class DenyForAllUser(BasePermission):
    def has_permission(self, request, view):
        return False