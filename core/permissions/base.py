from rest_framework.permissions import BasePermission
from .base import HasRole

# 1. Simple role checks using the base class
IsDoctor = HasRole(['doctor'])
IsNurse = HasRole(['nurse'])
IsHRAdmin = HasRole(['admin'])

# 2. Complex business logic middleware
class CanManageAttendance(BasePermission):
    """
    Doctors and Nurses can view their own attendance.
    Only HR/Admins can create or edit attendance records.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        user_role = request.auth.payload.get('role')

        # Read operations (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return user_role in ['doctor', 'nurse', 'admin']
            
        # Write operations (POST, PUT, PATCH, DELETE)
        return user_role in ['admin']