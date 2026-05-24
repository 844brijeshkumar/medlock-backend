from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from ..models import *
from ..serializers import *

# 1. SAAS & CORE ADMIN
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

# 2. PLUGIN & RBAC ENGINE
class PluginViewSet(viewsets.ModelViewSet):
    queryset = Plugin.objects.all()
    serializer_class = PluginSerializer

class AdminPluginViewSet(viewsets.ModelViewSet):
    queryset = AdminPlugin.objects.all()
    serializer_class = AdminPluginSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionMappingViewSet(viewsets.ModelViewSet):
    queryset = PermissionMapping.objects.all()
    serializer_class = PermissionMappingSerializer

class PermissionOverrideViewSet(viewsets.ModelViewSet):
    queryset = PermissionOverride.objects.all()
    serializer_class = PermissionOverrideSerializer

# 3. INFRASTRUCTURE & BIOMETRICS
class HospitalNetworkViewSet(viewsets.ModelViewSet):
    queryset = HospitalNetwork.objects.all()
    serializer_class = HospitalNetworkSerializer

class AdminNetworkViewSet(viewsets.ModelViewSet):
    queryset = AdminNetwork.objects.all()
    serializer_class = AdminNetworkSerializer

class BiometricDeviceMappingViewSet(viewsets.ModelViewSet):
    queryset = BiometricDeviceMapping.objects.all()
    serializer_class = BiometricDeviceMappingSerializer

# 4. HR, ATTENDANCE & DEPARTMENTS
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class ReceptionistViewSet(viewsets.ModelViewSet):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer

class BiometricPunchViewSet(viewsets.ModelViewSet):
    queryset = BiometricPunch.objects.all()
    serializer_class = BiometricPunchSerializer

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer

# 5. PATIENT ECOSYSTEM
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAppointmentViewSet(viewsets.ModelViewSet):
    queryset = UserAppointment.objects.all()
    serializer_class = UserAppointmentSerializer

class UserReportViewSet(viewsets.ModelViewSet):
    queryset = UserReport.objects.all()
    serializer_class = UserReportSerializer

class UserEventViewSet(viewsets.ModelViewSet):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

class UserBloodAppointmentViewSet(viewsets.ModelViewSet):
    queryset = UserBloodAppointment.objects.all()
    serializer_class = UserBloodAppointmentSerializer

class UserBloodDonationViewSet(viewsets.ModelViewSet):
    queryset = UserBloodDonation.objects.all()
    serializer_class = UserBloodDonationSerializer

# 6. NHCX CLAIMS & DISPATCH
class TpaProviderViewSet(viewsets.ModelViewSet):
    queryset = TpaProvider.objects.all()
    serializer_class = TpaProviderSerializer

class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

class ClaimMlcDetailViewSet(viewsets.ModelViewSet):
    queryset = ClaimMlcDetail.objects.all()
    serializer_class = ClaimMlcDetailSerializer

class ClaimMaternityDetailViewSet(viewsets.ModelViewSet):
    queryset = ClaimMaternityDetail.objects.all()
    serializer_class = ClaimMaternityDetailSerializer

class ClaimDocumentViewSet(viewsets.ModelViewSet):
    queryset = ClaimDocument.objects.all()
    serializer_class = ClaimDocumentSerializer

class ClaimDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = ClaimDiagnosis.objects.all()
    serializer_class = ClaimDiagnosisSerializer

class ClaimProcedureViewSet(viewsets.ModelViewSet):
    queryset = ClaimProcedure.objects.all()
    serializer_class = ClaimProcedureSerializer

class ClaimLabOrderViewSet(viewsets.ModelViewSet):
    queryset = ClaimLabOrder.objects.all()
    serializer_class = ClaimLabOrderSerializer

class ClaimPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = ClaimPrescription.objects.all()
    serializer_class = ClaimPrescriptionSerializer

class ClaimGovtPackageViewSet(viewsets.ModelViewSet):
    queryset = ClaimGovtPackage.objects.all()
    serializer_class = ClaimGovtPackageSerializer
