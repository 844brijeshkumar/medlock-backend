from rest_framework import serializers
from .models import *

# 1. SAAS & CORE ADMIN
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

# 2. PLUGIN & RBAC ENGINE
class PluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plugin
        fields = '__all__'

class AdminPluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPlugin
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionMapping
        fields = '__all__'

class PermissionOverrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionOverride
        fields = '__all__'

# 3. INFRASTRUCTURE & BIOMETRICS
class HospitalNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalNetwork
        fields = '__all__'

class AdminNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNetwork
        fields = '__all__'

class BiometricDeviceMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricDeviceMapping
        fields = '__all__'

# 4. HR, ATTENDANCE & DEPARTMENTS
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {'adhaar': {'write_only': True}}

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'
        extra_kwargs = {'adhaar': {'write_only': True}}

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'
        extra_kwargs = {'adhaar': {'write_only': True}}

class BiometricPunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricPunch
        fields = '__all__'

class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = '__all__'

# 5. PATIENT ECOSYSTEM
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'adhaar': {'write_only': True},
            'abha': {'write_only': True}
        }

class UserAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppointment
        fields = '__all__'

class UserReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReport
        fields = '__all__'

class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = '__all__'

class UserBloodAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBloodAppointment
        fields = '__all__'

class UserBloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBloodDonation
        fields = '__all__'

# 6. NHCX CLAIMS & DISPATCH
class TpaProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TpaProvider
        fields = '__all__'

class InsuranceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceProvider
        fields = '__all__'

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
        extra_kwargs = {'subscriber_govt_id': {'write_only': True}}

class ClaimMlcDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimMlcDetail
        fields = '__all__'

class ClaimMaternityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimMaternityDetail
        fields = '__all__'

class ClaimDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimDocument
        fields = '__all__'

class ClaimDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimDiagnosis
        fields = '__all__'

class ClaimProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimProcedure
        fields = '__all__'

class ClaimLabOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimLabOrder
        fields = '__all__'

class ClaimPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimPrescription
        fields = '__all__'

class ClaimGovtPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimGovtPackage
        fields = '__all__'