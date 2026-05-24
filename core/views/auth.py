from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import re

# Import all your models that can log in
from ..models import Admin, Hospital, Department, Ward, Room, Doctor, Nurse, Receptionist

class RoleBasedLoginView(APIView):
    """
    Handles POST requests to /api/<role>/login/ using Custom 12-digit IDs
    """
    permission_classes = [] 
    authentication_classes = []

    def post(self, request, role):
        # 1. Get the ID and password from the request. 
        # (Accepts "id", "username", or "user_id" from the frontend)
        provided_id = request.data.get("id") or request.data.get("username")
        password = request.data.get("password")

        if not provided_id or not password:
            return Response(
                {"error": "Please provide both id and password."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. Clean the ID: Strip out "Ad-", "Dr-", etc., leaving only the 12 digits
        # This turns "Ad-190080070011" into an integer: 190080070011
        numeric_id_str = re.sub(r'\D', '', str(provided_id))
        
        if not numeric_id_str:
            return Response(
                {"error": "Invalid ID format. Must contain the 12-digit number."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        numeric_id = int(numeric_id_str)
        role = role.lower()
        user_instance = None
        role_name = role

        # 3. Query the exact custom table based on the role in the URL
        try:
            if role in ["admin", "ad"]:
                user_instance = Admin.objects.get(id=numeric_id)
                role_name = "admin"
            elif role in ["hospital", "hp"]:
                user_instance = Hospital.objects.get(id=numeric_id)
            elif role in ["department", "dp"]:
                user_instance = Department.objects.get(id=numeric_id)
            elif role in ["ward", "wr"]  :
                user_instance = Ward.objects.get(id=numeric_id)
            elif role in ["room", "rm"]:
                user_instance = Room.objects.get(id=numeric_id)
            elif role in ["doctor", "dr"]:
                user_instance = Doctor.objects.get(id=numeric_id)
            elif role in ["nurse", "ns"]:
                user_instance = Nurse.objects.get(id=numeric_id)
            elif role in ["receptionist", "rs"]:
                user_instance = Receptionist.objects.get(id=numeric_id)
            else:
                return Response({"error": "Invalid login."}, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception: # Catches DoesNotExist
            return Response({"error": "User with this ID not found."}, status=status.HTTP_404_NOT_FOUND)

        # 4. Verify the password
        # (Since we set it to 'temp_password' in the database, we just do a direct string check. 
        # In the future, if you hash passwords, you will use check_password() here)
        if user_instance.password != password:
            return Response(
                {"error": "Invalid password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 5. Generate Custom JWT Token
        refresh = RefreshToken()
        refresh['user_id'] = user_instance.id
        refresh['role'] = role_name

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "role": role_name,
            "user_id": user_instance.id,
            "name": getattr(user_instance, 'name', 'Unknown')
        }, status=status.HTTP_200_OK)