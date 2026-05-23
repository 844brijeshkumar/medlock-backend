from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
# We register them so they show up in the Admin Dashboard

# 1. SAAS & CORE
admin.site.register(Subscription)
admin.site.register(Admin)
admin.site.register(Hospital)

# 2. PLUGIN & RBAC
admin.site.register(Plugin)
admin.site.register(AdminPlugin)
admin.site.register(Permission)
admin.site.register(PermissionMapping)
admin.site.register(PermissionOverride)

# 3. INFRASTRUCTURE & BIOMETRICS
admin.site.register(HospitalNetwork)
admin.site.register(AdminNetwork)
admin.site.register(BiometricDeviceMapping)

# 4. HR, ATTENDANCE & DEPARTMENTS
admin.site.register(Department)
admin.site.register(Ward)
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Receptionist)
admin.site.register(BiometricPunch)
admin.site.register(StaffAttendance)

# 5. PATIENT ECOSYSTEM
admin.site.register(User)
admin.site.register(UserAppointment)
admin.site.register(UserReport)
admin.site.register(UserEvent)
admin.site.register(UserBloodAppointment)
admin.site.register(UserBloodDonation)

# 6. NHCX CLAIMS & DISPATCH
admin.site.register(TpaProvider)
admin.site.register(InsuranceProvider)
admin.site.register(Claim)
admin.site.register(ClaimMlcDetail)
admin.site.register(ClaimMaternityDetail)
admin.site.register(ClaimDocument)
admin.site.register(ClaimDiagnosis)
admin.site.register(ClaimProcedure)
admin.site.register(ClaimLabOrder)
admin.site.register(ClaimPrescription)
admin.site.register(ClaimGovtPackage)