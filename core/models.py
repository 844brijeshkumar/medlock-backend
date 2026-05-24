# core/models.py
from django.db import models
from django.db.models import Q

# =============================================================================
# BASE ABSTRACT MODEL (For 12-Digit Custom IDs)
# =============================================================================
class CustomIDModel(models.Model):
    """
    Abstract model that replaces the default auto-incrementing ID with a 
    12-digit BigIntegerField starting at 190080070011.
    """
    id = models.BigIntegerField(primary_key=True, editable=False)

    class Meta:
        abstract = True # Tells Django NOT to create a table for this class

    def save(self, *args, **kwargs):
        if not self.id:  # Only generate if this is a new record
            # self.__class__ dynamically looks at whichever model is being saved
            last_record = self.__class__.objects.order_by('-id').first()
            if last_record:
                self.id = last_record.id + 1
            else:
                self.id = 190080070011
        super().save(*args, **kwargs)


# =============================================================================
# 1. SAAS & CORE ADMIN
# =============================================================================

class Subscription(models.Model):
    tier_name = models.CharField(max_length=100, unique=True)
    max_branches = models.IntegerField()
    max_staffs = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.tier_name

class Theme(models.Model):
    name = models.CharField(max_length=100)
    primary = models.CharField(max_length=7, null=True)
    secondary = models.CharField(max_length=7, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Updated to use CustomIDModel
class Admin(CustomIDModel):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Updated to use CustomIDModel
class Hospital(CustomIDModel):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    location = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# =============================================================================
# 2. PLUGIN & RBAC ENGINE
# =============================================================================

class Plugin(models.Model):
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=3, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AdminPlugin(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    activated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('admin', 'plugin')

class Permission(models.Model):
    name = models.CharField(max_length=100)
    suburl = models.CharField(max_length=100)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PermissionMapping(models.Model):
    role = models.CharField(max_length=3)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    requires_on_premise = models.BooleanField(default=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('role', 'permission')

class PermissionOverride(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    staff_type = models.CharField(max_length=3)
    staff_id = models.CharField(max_length=50) 
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    is_allowed = models.BooleanField()
    assigned_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('staff_id', 'staff_type', 'permission')


# =============================================================================
# 3. INFRASTRUCTURE & BIOMETRICS
# =============================================================================

class HospitalNetwork(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    cidr_block = models.CharField(max_length=50)
    network_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

class AdminNetwork(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    cidr_block = models.CharField(max_length=50)
    network_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

class BiometricDeviceMapping(models.Model):
    device_ip = models.CharField(max_length=50)
    punch_id = models.IntegerField()
    staff_role = models.CharField(max_length=3)
    staff_id = models.BigIntegerField()
    is_currently_assigned = models.BooleanField(default=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    unassigned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['device_ip', 'punch_id'],
                condition=Q(is_currently_assigned=True),
                name='idx_unique_active_punch'
            )
        ]


# =============================================================================
# 4. HR, ATTENDANCE & DEPARTMENTS
# =============================================================================

# Updated to use CustomIDModel
class Department(CustomIDModel):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    building_id = models.CharField(max_length=50, null=True, blank=True)
    floor = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Updated to use CustomIDModel
class Ward(CustomIDModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Updated to use CustomIDModel
class Room(CustomIDModel):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_identifier = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

# Updated to use CustomIDModel
class Doctor(CustomIDModel):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    adhaar = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    gmail = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    punch_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Updated to use CustomIDModel
class Nurse(CustomIDModel):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    adhaar = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    gmail = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    punch_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

# Updated to use CustomIDModel
class Receptionist(CustomIDModel):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    adhaar = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    gmail = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    punch_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

class BiometricPunch(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    device_ip = models.CharField(max_length=50, null=True, blank=True)
    punch_id = models.IntegerField()
    punch_time = models.DateTimeField(auto_now_add=True)
    punch_type = models.CharField(max_length=10, null=True, blank=True)

class StaffAttendance(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff_role = models.CharField(max_length=3)
    staff_id = models.BigIntegerField()
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default='Present')

    class Meta:
        unique_together = ('staff_id', 'date')


# =============================================================================
# 5. PATIENT ECOSYSTEM
# =============================================================================

class User(models.Model):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gmail = models.EmailField(max_length=100, null=True, blank=True)
    adhaar = models.CharField(max_length=20, unique=True, null=True, blank=True)
    abha = models.CharField(max_length=20, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=50, default='SCHEDULED')

class UserReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    report_type = models.CharField(max_length=100, null=True, blank=True)
    report_payload = models.JSONField(null=True, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    event_description = models.TextField(null=True, blank=True)
    event_time = models.DateTimeField(auto_now_add=True)

class UserBloodAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=50, default='PENDING')

class UserBloodDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True, blank=True)
    blood_group = models.CharField(max_length=5)
    quantity_ml = models.IntegerField(default=450)
    donation_date = models.DateTimeField(auto_now_add=True)


# =============================================================================
# 6. NHCX CLAIMS & DISPATCH
# =============================================================================

class TpaProvider(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class InsuranceProvider(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, default='Retail')
    nhcx_routing_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Claim(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(UserAppointment, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    
    plan_type = models.CharField(max_length=50, default='Retail')
    provider = models.ForeignKey(InsuranceProvider, on_delete=models.SET_NULL, null=True, blank=True)
    is_routed_via_tpa = models.BooleanField(default=False)
    tpa = models.ForeignKey(TpaProvider, on_delete=models.SET_NULL, null=True, blank=True)
    
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    relationship_to_subscriber = models.CharField(max_length=50, default='Self')
    subscriber_name = models.CharField(max_length=150, null=True, blank=True)
    subscriber_govt_id = models.CharField(max_length=50, null=True, blank=True)
    
    clinical_notes = models.TextField(null=True, blank=True)
    necessity_justification = models.TextField(null=True, blank=True)
    patient_identity_verified_at = models.DateTimeField(null=True, blank=True)
    
    discharge_type = models.CharField(max_length=50, default='Routine')
    is_mlc = models.BooleanField(default=False)
    is_maternity = models.BooleanField(default=False)
    
    nhcx_claim_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    clinical_status = models.CharField(max_length=50, default='Draft')
    adminal_status = models.CharField(max_length=50, default='Pending Bill')
    claim_status = models.CharField(max_length=50, null=True, blank=True)
    auditor_query_note = models.TextField(null=True, blank=True)
    
    invoice_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    total_cgst = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_sgst = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    invoice_generated_at = models.DateTimeField(null=True, blank=True)
    total_billed_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    clinical_payload = models.JSONField(null=True, blank=True)
    admin_payload = models.JSONField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClaimMlcDetail(models.Model):
    claim = models.OneToOneField(Claim, on_delete=models.CASCADE, primary_key=True)
    fir_number = models.CharField(max_length=100)
    police_station = models.CharField(max_length=150)
    cause_of_injury = models.CharField(max_length=255, null=True, blank=True)

class ClaimMaternityDetail(models.Model):
    claim = models.OneToOneField(Claim, on_delete=models.CASCADE, primary_key=True)
    delivery_date = models.DateField()
    delivery_type = models.CharField(max_length=50, default='Normal')
    living_children = models.IntegerField(default=0)

class ClaimDocument(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    uploaded_by_role = models.CharField(max_length=3)
    uploaded_by_id = models.BigIntegerField()
    document_type = models.CharField(max_length=50)
    document_mode = models.CharField(max_length=10, default='FILE')
    file_url = models.TextField(null=True, blank=True)
    file_size_kb = models.IntegerField(null=True, blank=True)
    document_text = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ClaimDiagnosis(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    icd_code = models.CharField(max_length=20)
    description = models.TextField()
    priority = models.CharField(max_length=50, default='Medium')
    billing_diag_type = models.CharField(max_length=50, null=True, blank=True)
    service_type = models.CharField(max_length=20, null=True, blank=True)
    room_type = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

class ClaimProcedure(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    procedure_code = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=50, default='Routine')
    billing_type = models.CharField(max_length=50, null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    sac_code = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

class ClaimLabOrder(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    loinc_code = models.CharField(max_length=50)
    description = models.TextField()
    sac_code = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

class ClaimPrescription(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    drug_code = models.CharField(max_length=50)
    description = models.TextField()
    item_type = models.CharField(max_length=50)
    hsn_code = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=12.00)
    added_at = models.DateTimeField(auto_now_add=True)

class ClaimGovtPackage(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    package_code = models.CharField(max_length=50)
    package_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    mapped_at = models.DateTimeField(auto_now_add=True)