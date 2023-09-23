from rest_framework.permissions import BasePermission


class MyPermissionClass(BasePermission):
    
    message = "You are not allowed to perform this action : MyPermissionClass"
    
    # which should return either true or false
    def has_permission(self, request, view):
        return False
    
