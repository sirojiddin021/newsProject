from rest_framework.permissions import BasePermission
import news.models as models

class IsAdminOrAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == '1' or request.user.role == '2':
            return True
        
