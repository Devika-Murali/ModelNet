from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(blank=True, null=True) 
    age = models.IntegerField(null=True, blank=True)  
    place = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True) 
    reset_password=models.CharField(max_length=128,null=True,blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)   
    medical_history = models.FileField(upload_to='medical_history/', null=True, blank=True)
    def __str__(self):
        return self.name
class Specialization(models.Model):
    specialization_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.specialization_name


class Docprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'),('Others', 'Others')],null=True, blank=True) 
    dob = models.CharField(max_length=100, null=True, blank=True)
    add1 = models.CharField(max_length=100, null=True, blank=True)
    add2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postalcode = models.CharField(max_length=100, null=True, blank=True)
    services = models.TextField( null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    degree= models.CharField(max_length=100, null=True, blank=True)
    college = models.TextField(null=True, blank=True)
    cyear=models.CharField(max_length=100, null=True, blank=True)
    hospital_name= models.TextField( null=True, blank=True)
    from_date=models.CharField(max_length=100, null=True, blank=True)
    to_date=models.CharField(max_length=100, null=True, blank=True)
    award = models.TextField(null=True, blank=True)
    ayear=models.CharField(max_length=100, null=True, blank=True)

    specialist = models.ForeignKey(Specialization, on_delete=models.CASCADE,  null=True, blank=True)  # Reference to the category
    reset_password=models.CharField(max_length=128,null=True,blank=True)

# class MedicalRecord(models.Model):
#     diagnosis_date = models.DateField()
#     cancer_stage = models.CharField(max_length=255)
#     biopsy_results = models.TextField()
#     oncologist_name = models.CharField(max_length=255)
#     allergy_name = models.CharField(max_length=255)
#     allergy_severity = models.CharField(
#         max_length=10,
#         choices=[
#             ('mild', 'Mild'),
#             ('moderate', 'Moderate'),
#             ('severe', 'Severe'),
#         ]
#     )
#     medication_name = models.CharField(max_length=255)
#     dosage = models.CharField(max_length=50)
#     frequency = models.CharField(max_length=50)
#     start_date = models.DateField()

#     def __str__(self):
#         return f"Medical Record ({self.diagnosis_date})"
# class PatientInfo(models.Model):
#     # Medical History Fields
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
#     diagnosis_date = models.DateField(null=True, blank=True)
#     cancer_stage = models.CharField(max_length=255, blank=True)
#     biopsy_results = models.TextField(blank=True)
#     oncologist_name = models.CharField(max_length=255, blank=True)

#     # Allergies Fields
#     allergy_name = models.CharField(max_length=255, blank=True)
#     allergy_severity = models.CharField(
#         max_length=10,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')],
#         blank=True
#     )

#     # Medications Fields
#     medication_name = models.CharField(max_length=255, blank=True)
#     dosage = models.CharField(max_length=255, blank=True)
#     frequency = models.CharField(max_length=255, blank=True)
#     start_date = models.DateField(null=True, blank=True)
    
#     # Add more fields as needed

#     def __str__(self):
#         return f"Patient Information - {self.pk}"
class PatientInfo(models.Model):
    # Medical History Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    diagnosis_date = models.DateField(null=True, blank=True)
    biopsy_results = models.FileField(upload_to='biopsy_results/', blank=True)  # Changed to FileField for file upload

    # Allergies Fields
    presenting_symptoms = models.CharField(max_length=255, blank=True)  # Renamed from 'allergy_name'
    allergies = models.CharField(max_length=255, blank=True)  # Renamed from 'allergy_severity'

    # Diagnostic Workup Fields
    colonoscopy_date = models.DateField(null=True, blank=True)
    colonoscopy_findings = models.CharField(max_length=255, blank=True)
    ct_scan_results = models.FileField(upload_to='ct_scan_results/', blank=True)  # Added for CT scan results

    # Treatment History Fields
    treatment_plan = models.CharField(max_length=255, blank=True)
    date_of_initiation = models.DateField(null=True, blank=True)
    response_to_treatment = models.CharField(max_length=255, blank=True)
    complications = models.CharField(max_length=255, blank=True)

    # Add more fields as needed

    def __str__(self):
        return f"Patient Information - {self.pk}"

# class Docs(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
#     Dep_id = models.ForeignKey(Deps, on_delete=models.CASCADE)
#     Name = models.CharField(max_length=110)
#     dob = models.CharField(max_length=50, blank=True, null=True)
#     city = models.TextField()
#     address = models.CharField(max_length=50, blank=True, null=True)
#     phn = models.IntegerField()
#     gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], blank=True, null=True)
#     state = models.CharField(max_length=100, null=True, blank=True)
#     country = models.CharField(max_length=100, null=True, blank=True)
    
# def _str_(self):
#         return self.Name
# 
class Certification(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'
    
    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    ]
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default=Seller)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    certification_image = models.ImageField(upload_to='certification_image/', null=True, blank=True)
    doctor_name = models.CharField(max_length=100, null=True, blank=True)  # Change 'first_name' to 'owner_name'
    specialization = models.CharField(max_length=100, null=True, blank=True)  # Add 'store_name' field
    expiry_date_to = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )
 
from django.db import models

# class Timeslot(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return f"{self.user.email} - {self.date} {self.start_time}-{self.end_time}"
class Slots(models.Model):
    doctor = models.ForeignKey(Docprofile, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"Slot for Dr. {self.doctor.name} on {self.date} at {self.start_time}-{self.end_time}"

# class Appointment(models.Model):
#     fullName = models.CharField(max_length=100,null=True, blank=True)

#     age = models.IntegerField(null=True, blank=True)
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other'),
#     ]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True, blank=True)
#     phone = models.CharField(max_length=15,null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     doctor = models.ForeignKey(Docprofile, on_delete=models.CASCADE, related_name='appointments') 
#     symptoms = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     app_date = models.DateField(null=True, blank=True)
#     app_time = models.TimeField(null=True, blank=True)
class Appointments(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    doctor = models.ForeignKey(Docprofile, on_delete=models.CASCADE, related_name='appointments') 
    appointment_type = models.CharField(max_length=100,null=True, blank=True)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    reason = models.TextField(blank=True, null=True)
 


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True, null=True)  # Use auto_now_add=True for initial creation


    def _str_(self):
        return f"Payment ID: {self.id}, Status: {self.payment_status}"

class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('emergency', 'Emergency Leave'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    doctor_name = models.CharField(max_length=100, default='')

    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    leave_reason = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, null=True,blank=True, default='pending')
    def __str__(self):
        return f"{self.get_leave_type_display()} - {self.start_date} to {self.end_date}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.ImageField(upload_to='blog_images/', verbose_name='Blog Images', null=True, blank=True)
    blog_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.title

class ReferPatient(models.Model):
    hospital_name = models.CharField(max_length=100,null=True,blank=True)
    patient_name = models.CharField(max_length=100,null=True,blank=True)
    referring_doctor = models.ForeignKey(Docprofile, on_delete=models.CASCADE,null=True,blank=True) 
    referring_doctor_name = models.CharField(max_length=100,null=True,blank=True)
    referring_doctor_email = models.EmailField(max_length=100,null=True,blank=True)
    medical_details = models.FileField(upload_to='medical_details/%Y/%m/%d/')
    case_sheet = models.FileField(upload_to='case_sheets/%Y/%m/%d/',null=True,blank=True)
    comments = models.TextField(null=True,blank=True)
    referred_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    accept = models.BooleanField(default=False)

class Donation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    place = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation #{self.pk}: {self.full_name} - {self.amount}"

class Prescription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    medication_name = models.CharField(max_length=100)
    dosage_strength = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=50)
    route_of_admin = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    special_instructions = models.TextField()

    def __str__(self):
        return self.medication_name