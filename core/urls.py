from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# The router automatically generates endpoints for all your ViewSets
router = DefaultRouter()

# 1. SAAS & CORE ADMIN
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'hospitals', HospitalViewSet)

# 2. PLUGIN & RBAC ENGINE
router.register(r'plugins', PluginViewSet)
router.register(r'admin-plugins', AdminPluginViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'permission-mappings', PermissionMappingViewSet)
router.register(r'permission-overrides', PermissionOverrideViewSet)

# 3. INFRASTRUCTURE & BIOMETRICS
router.register(r'hospital-networks', HospitalNetworkViewSet)
router.register(r'admin-networks', AdminNetworkViewSet)
router.register(r'biometric-device-mappings', BiometricDeviceMappingViewSet)

# 4. HR, ATTENDANCE & DEPARTMENTS
router.register(r'departments', DepartmentViewSet)
router.register(r'wards', WardViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'beds', BedViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)
router.register(r'receptionists', ReceptionistViewSet)
router.register(r'biometric-punches', BiometricPunchViewSet)
router.register(r'staff-attendance', StaffAttendanceViewSet)

# 5. PATIENT ECOSYSTEM
router.register(r'users', UserViewSet)
router.register(r'user-appointments', UserAppointmentViewSet)
router.register(r'user-reports', UserReportViewSet)
router.register(r'user-events', UserEventViewSet)
router.register(r'user-blood-appointments', UserBloodAppointmentViewSet)
router.register(r'user-blood-donations', UserBloodDonationViewSet)

# 6. NHCX CLAIMS & DISPATCH
router.register(r'tpa-providers', TpaProviderViewSet)
router.register(r'insurance-providers', InsuranceProviderViewSet)
router.register(r'claims', ClaimViewSet)
router.register(r'claim-mlc-details', ClaimMlcDetailViewSet)
router.register(r'claim-maternity-details', ClaimMaternityDetailViewSet)
router.register(r'claim-documents', ClaimDocumentViewSet)
router.register(r'claim-diagnoses', ClaimDiagnosisViewSet)
router.register(r'claim-procedures', ClaimProcedureViewSet)
router.register(r'claim-lab-orders', ClaimLabOrderViewSet)
router.register(r'claim-prescriptions', ClaimPrescriptionViewSet)
router.register(r'claim-govt-packages', ClaimGovtPackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]