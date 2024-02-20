from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout,get_user_model
from .models import UserProfile,Docprofile,Specialization,Certification,Appointments
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from .models import PatientInfo 
from .models import Specialization,Payment,LeaveApplication
from torchvision import transforms
from django.http import JsonResponse

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from django.contrib.auth.decorators import login_required
def Home(request):
    doctors= Docprofile.objects.all()
    print(doctors)
    return render(request,'Home.html',{'doctors':doctors})
def About(request):
    return render(request,'About.html')  
def basepatient(request):
    return render(request,'basepatient.html')

def doctors_basedoctor(request):
    user_id = request.user.id

    # Filter the Docprofile instance associated with the current user
    me = Docprofile.objects.filter(user_id=user_id).first()  # Use first() to get a single instance or None

    # If the Docprofile instance exists for the current user
    if me:
        # Count the number of ReferPatient instances where the referring_doctor matches the Docprofile instance
        count = ReferPatient.objects.filter(referring_doctor=me).count()
    
        
        # Render the template with the count
        # return render(request, 'doctors_basedoctor.html', {'count': count})
    else:
        # Handle the case where Docprofile does not exist for the current user
        # You can render an appropriate error message or redirect to a page
        pass
    
    existing_certification = Certification.objects.filter(user=request.user).first()

    if existing_certification:
        return render(request, 'doctors/basedoctor.html', {'existing_certification': existing_certification, 'count': count})

    if request.method == 'POST':
        # Handle form submission
        certification_image = request.FILES.get('certification_image')
        owner_name = request.POST.get('owner_name')
        specialization = request.POST.get('specialization')
        expiry_date_to = request.POST.get('expiry_date_to')

        # if not certification_image or not owner_name or not store_name or not expiry_date_from or not expiry_date_to:
        #     messages.error(request, 'Please fill in all required fields.')
        # else:
            # Create and save the Certification instance
        certification = Certification(
            user=request.user,
            certification_image=certification_image,
            doctor_name=owner_name,
            specialization=specialization,
            expiry_date_to=expiry_date_to,
        )
        certification.save()
        return redirect('doctors_basedoctor')  

    return render(request,'doctors/basedoctor.html', {
        'existing_certification': existing_certification,
    })

    return render(request,'doctors_basedoctor.html' ,{'count': count}) 


    
# def doctors_timeslot(request):
#     return render(request,'doctors/timeslot.html')
def doctors_testresult(request):
    return render(request,'doctors/testresult.html')  

# def doctors_timeslotdisplay(request):
#     return render(request,'doctors/timeslotdisplay.html') 
def testresult(request):
    return render(request,'testresult.html') 
     


def mypatients(request):
    users = User.objects.all()
    return render(request,'mypatients.html', {'users': users})  
def patientprofile(request):
    return render(request,'patientprofile.html')     
def profileset(request):
    return render(request,'profileset.html')  
def DoctorProfileView(request):
    return render(request, 'doctor_profile.html')
def admins_index(request):
    return render(request, 'admins/index.html')
def admins_registereduser(request):
    return render(request, 'admins/registereduser.html')
def admins_blogs(request):
    return render(request, 'admins/blog.html')

def admins_patientlist(request):
    # Retrieve the list of patients (users) from the database
    patients = User.objects.filter(is_superuser=False, is_staff=False)

    # Pass the list of patients to the template
    return render(request, 'admins/patientlist.html', {'users': patients})

def admins_appointmentlist(request):
    appointments = Appointment.objects.all()
    return render(request, 'admins/appointmentlist.html',{'appointments':appointments})


def patient_medicalhistory(request):
    current_user = request.user
    patient_info = PatientInfo.objects.get(user=current_user)

    # Pass the patient_info object to the template context
    context = {
        'patient_info': patient_info,
    }
    return render(request, 'patient/medicalhistory.html',context)
def patient_finddoctor(request):
    doctors = Docprofile.objects.all()
    print(doctors)
    return render(request, 'patient/finddoctor.html',{'doctors':doctors})
def Doctor_patienthistory(request):
    return render(request,'Doctor/patienthistory.html')   
def patientappointment(request):
    return render(request, 'patientappointment.html')    
def scheduletiming(request):
    return render(request, 'scheduletiming.html')
def patientbooking(request):
    return render(request, 'patientbooking.html')
def patientprofileset(request):
    return render(request, 'patientprofileset.html')
def adddoctor(request):
    return render(request,'Admin Dashboard/add-doctor.html')
def admins_doctorlist(request):
    return render(request, 'admins/doctorlist.html')
def edit_records_view(request, patient_id):
    # Retrieve the patient based on the patient_id, or handle errors gracefully
    patient = get_object_or_404(User, id=patient_id)

    return render(request, 'doctors/editrecords.html', {'patient': patient})

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                request.session['user_id'] = user.id
                request.session['username'] = user.email
                return redirect('admins_index')
            elif user.is_staff:
                request.session['user_id'] = user.id
                request.session['username'] = user.email
                return redirect('doctors_basedoctor')
            else:
                request.session['user_id'] = user.id
                request.session['username'] = user.email
                return redirect('basepatient')
        else:
            messages.error(request, 'No user found with the provided credentials.')
    return render(request, 'Login.html')
# 
# def login_page(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # Authentication successful
#             if not user.is_superuser and not user.is_staff:
#                 request.session['user_id'] = user.id
#                 request.session['username'] = user.email
#                 return redirect('basepatient')
#             elif user.is_superuser:
#                 return redirect('admin_index')
#             elif user.is_staff:
#                 # Handle staff members differently, e.g., redirect to a staff dashboard.
#                 return redirect('staff_dashboard')
#         else:
#             messages.error(request, 'Password is incorrect. Please try again.')

#     return render(request, 'Login.html')


@login_required
def admins_registereduser(request):
    users = User.objects.all()
    return render(request, 'admins/registereduser.html', {'users': users})
@login_required
def edituser(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Handle form submission and update user details
        user.username = request.POST['username']
        user.email = request.POST['email']

        # Update user role based on the selected role option
        role = request.POST.get('role')
        if role == 'customer':
            user.is_staff = False
            user.is_superuser = False
        elif role == 'staff':
            user.is_staff = True
            user.is_superuser = False
        elif role == 'superuser':
            user.is_staff = True
            user.is_superuser = True

        user.save()
        messages.success(request, "User details updated successfully.")
        return redirect('userlist')  # Redirect back to the user list page
    return render(request, 'Admin/edituser.html', {'user': user})

def register(request):
    
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email = email,password=password)
                user_profile=UserProfile(user=user, email=email, name=name)
                user_profile.save()
                patient_info=PatientInfo.objects.create(user=user)
                messages.info(request, "Registered Succesfully")
                print(user)
                print(user_profile)
                print(patient_info)
                return redirect('login_page')
        else:
            messages.info(request, " ")
            return redirect('register')
    return render(request, 'register.html')


def DoctorReg(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        select_category_id = request.POST.get('select_category')
        category = Specialization.objects.get(id=select_category_id)
                                                     
        print(select_category_id)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)   
                doc_profile = Docprofile.objects.create(user=user, name=name, email=email, specialist=category)
                doc_profile.save()
                user.is_staff = True
                user.save()
                messages.info(request, "Registered Successfully")
                return redirect('login_page')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('DoctorReg')
    categories = Specialization.objects.all()

    return render(request, 'DoctorReg.html',{'categories': categories})

def loggout(request):
    print('Logged Out')
    logout(request)
    if 'username' in request.session:
        del request.session['username']
        request.session.clear()
    return redirect('Home5')


def profile(request):
    print("jd")
    user_profile = UserProfile.objects.get(user=request.user)
    print(request.user)
    if request.method == 'POST':
        # Retrieve form data using the correct field names
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        email = request.POST.get('email')  # You missed this field in your code
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        place = request.POST.get('place')
        state = request.POST.get('state')
        country = request.POST.get('country')
        blood_group = request.POST.get('blood_group')
        gender = request.POST.get('gender')
        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')
        # Retrieve profile picture and medical history files
       
        
        medical_history = request.FILES.get('new_medical_history')

        # Update user_profile fields
        user_profile.fname = fname
        user_profile.lname = lname
        user_profile.age = age
        user_profile.email = email
        user_profile.phone_number = phone_number
        user_profile.address = address
        user_profile.place = place
        user_profile.state = state
        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES.get['profile_pic']
            user_profile.profile_pic = profile_pic
            print('got')
        user_profile.country = country
        user_profile.blood_group = blood_group
        user_profile.gender = gender

        # Handle profile picture and medical history files
        
        if medical_history:
            user_profile.medical_history = medical_history
        if request.user.check_password(old_password):
            #  the old password is correct, set the new password
                request.user.set_password(reset_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
        else:
            messages.error(request, "Incorrect old password. Password not updated.")
        
        
        user_profile.reset_password = reset_password
        user_profile.save()
        messages.success(request, "Profile updated successfully")
        return redirect('patientprofileset')

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'patientprofileset.html', context)

@require_POST
def delete_specialization(request):
    try:
        specialization_id = request.POST.get('specialization_id')
        specialization = Specialization.objects.get(id=specialization_id)
        specialization.delete()
        response_data = {'success': True, 'message': 'Specialization deleted successfully'}
    except Exception as e:
        response_data = {'success': False, 'message': str(e)}
    return JsonResponse(response_data)

def DoctorProfileView(request):
    doc_profile = Docprofile.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile_pic= request.POST.get('profile_pic')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        phone= request.POST.get('phone')
        gender= request.POST.get('gender')
        dob= request.POST.get('dob')
        add1= request.POST.get('add1')
        add2= request.POST.get('add2')
        city= request.POST.get('city')
        state= request.POST.get('state')
        country= request.POST.get('country')
        postalcode= request.POST.get('postalcode')
        services= request.POST.get('services')
        specialist= request.POST.get('specialist')
        about=request.POST.get('about')
        degree=request.POST.get('degree')
        college=request.POST.get('college')
        cyear=request.POST.get('cyear')
        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')
        
        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES['profile_pic']
            doc_profile.profile_pic = profile_pic
            print('got')
        doc_profile.name = name
        doc_profile.phone = phone
        doc_profile.fname = fname
        doc_profile.lname = lname
        doc_profile.gender = gender
        doc_profile.dob = dob
        doc_profile.add1 = add1
        doc_profile.add2 = add2
        doc_profile.city = city
        doc_profile.state = state
        doc_profile.country = country
        doc_profile.postalcode = postalcode
        doc_profile.services = services
        doc_profile.specialist = specialist
        doc_profile.about = about
        doc_profile.degree = degree
        doc_profile.college = college
        doc_profile.cyear = cyear
        if request.user.check_password(old_password):
            #  the old password is correct, set the new password
                request.user.set_password(reset_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
        else:
            messages.error(request, "Incorrect old password. Password not updated.")
        
        
        doc_profile.reset_password = reset_password
        doc_profile.save()
        request.user.save()
        
        return redirect('profileset') 

    context = {
        'doc_profile': doc_profile,
        'profile_pic_url': doc_profile.profile_pic.url if doc_profile.profile_pic else None
    }
    
    return render(request, 'profileset.html', context)
def admin_adddoctor(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        Name= request.POST.get('Name')
        email= request.POST.get('email')
        password = request.POST.get('password')
        phn= request.POST.get('phn')
        dep_id = request.POST.get('depp')
        role=CustomUser.DOCTOR
        print(role)
        if CustomUser.objects.filter(email=email,role=CustomUser.DOCTOR).exists():
                messages.info(request, 'Email already exists') 
                return redirect('admin_adddoctor')
        else:
                user = CustomUser.objects.create_user(email=email, password=password)
                user.role = CustomUser.DOCTOR
                user.save()
                doctor = Docs(user=user,Name=Name,Dep_id_id=dep_id,phn=phn)
                doctor.save()

                
                subject = 'Doctor Login Details'
                message = f'Registered as an Doctor. Your username: {email}, Password: {password}'
                from_email = settings.EMAIL_HOST_USER  
                recipient_list = [user.email]  

                send_mail(subject, message, from_email, recipient_list)

                return redirect('admin_doctors')
    else:
        depts = Deps.objects.all()
        context = {  'depts': depts}
        return render(request, 'admin_adddoctor.html', context)

@login_required
def specializations(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            # Add a new specialization
            specialization_name = request.POST.get('specialization_name')
            formatted_specialization_name = specialization_name.capitalize()
            try:
                Specialization.objects.create(specialization_name=formatted_specialization_name)
                messages.success(request, 'Specialization created successfully.')
            except Exception as e:
                messages.error(request, 'Error creating specialization: {}'.format(str(e)))

        elif action == 'edit':
            try:
                # Edit an existing specialization
                specialization_id = request.POST.get('specialization_id')
                specialization = get_object_or_404(Specialization, pk=specialization_id)
                new_specialization_name = request.POST.get('specialization_name')

                if Specialization.objects.filter(specialization_name=new_specialization_name).exclude(id=specialization.id).exists():
                    messages.error(request, 'Specialization with this name already exists.')
                else:
                    specialization.specialization_name = new_specialization_name
                    specialization.save()
                    messages.success(request, 'Specialization updated successfully.')
            except Exception as e:
                messages.error(request, 'An error occurred during specialization update: {}'.format(str(e)))


        elif action == 'delete':
            # Delete an existing specialization
            specialization_id = request.POST.get('specialization_id')
            specialization = get_object_or_404(Specialization, pk=specialization_id)
            specialization.delete()
            messages.success(request, 'Specialization deleted successfully.')

    # Get all specializations for displaying in the template
    specializations = Specialization.objects.filter(status=False)
    return render(request, 'admins/specialities.html', {'specializations': specializations})
   
#patient data
from django.shortcuts import render, redirect, get_object_or_404


def edit_specialization(request, specialization_id):
    specialization = get_object_or_404(Specialization, pk=specialization_id)

    if request.method == 'POST':
        new_specialization_name = request.POST.get('specialization_name')
        specialization.specialization_name = new_specialization_name
        specialization.save()
        return redirect('admins_specialities')  # Redirect to a relevant page after editing

@login_required
def dashlegal(request):
    # Retrieve Certification objects including their IDs
    seller_applications = Certification.objects.all()
    today = timezone.now().date()

    # Retrieve User roles for each Certification applicant
    user_roles = {}
    for application in seller_applications:
        # Ensure the user associated with the Certification exists
        user = get_object_or_404(User, id=application.user_id)

        # Retrieve user roles
        user_roles[application.id] = {
            'is_admin': user.is_superuser,
            'is_patient': user,
            'is_doctor': user.is_staff
        }

    context = {
        'seller_applications': seller_applications,
        'user_roles': user_roles,  # Include user roles in the context
        'today': today,
    }
    return render(request, 'admins/dashlegal.html', context)

def approve_certification(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = Certification.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('admins_dashlegal')

def reject_certification(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = Certification.REJECTED  # Set it to 'rejected'
        certification.save()
    return redirect('admins_dashlegal')

def submit_medical_history(request,patient_id):
    user = User.objects.get(id=patient_id)
    patient = UserProfile.objects.get(user=user)
    patient_info = PatientInfo.objects.get(user=user)
    if request.method == 'POST':
        # Retrieve data from the form
        diagnosis_date = request.POST.get('diagnosis_date')
        cancer_stage = request.POST.get('cancer_stage')
        biopsy_results = request.POST.get('biopsy_results')
        oncologist_name = request.POST.get('oncologist_name')
        allergy_name = request.POST.get('allergy_name')
        allergy_severity = request.POST.get('allergy_severity')
        medication_name = request.POST.get('medication_name')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        start_date = request.POST.get('start_date')
        # Create a new instance of the PatientInfo model and save it
           # Associate the data with the patient identified by patient_id

        patient_info.diagnosis_date = diagnosis_date
        patient_info.cancer_stage = cancer_stage
        patient_info.biopsy_results = biopsy_results
        patient_info.oncologist_name = oncologist_name
        patient_info.allergy_name = allergy_name
        patient_info.allergy_severity = allergy_severity
        patient_info.medication_name = medication_name
        patient_info.dosage = dosage
        patient_info.frequency = frequency
        patient_info.start_date = start_date

        
        patient_info.save()
        patient.save()
        # Redirect to the 'editrecords' URL after successful submission
        return redirect('mypatients')
 

    # Handle GET request or invalid submissions here
    return render(request, 'doctors/editrecords.html',{'patient':patient,'patient_info':patient_info})
def doctor_list(request):
    # Retrieve a list of doctor objects from the database
    doctors = Docprofile.objects.all()

    # Pass the list of doctors to the template
    return render(request, 'finddoctor.html', {'doctors': doctors})
# @login_required
# def add_timeslot(request):
#     if request.method == 'POST':
#         doctor_name = request.user.Docprofile  # Assuming you have a DoctorProfile model
#         date = request.POST['date']
#         start_time = request.POST['start_time']
#         end_time = request.POST['end_time']
#         Timeslot.objects.create(doctor_name=doctor_name, date=date, start_time=start_time, end_time=end_time)
#         return redirect('doctors_timeslot')
    
#     return render(request, 'doctors_timeslot.html')

# @login_required
# def doctor_timeslots(request):
#     doctor_name = request.user.docprofile  # Assuming you have a DoctorProfile model
#     timeslots = Timeslot.objects.filter(doctor_name=doctor_name)
#     return render(request, 'timeslotdisplay.html', {'timeslots': timeslots})
#liyak
# def add_timeslot(request):
#     # Check if a 'Docs' object exists for the logged-in user
#     try:
#         logged_in_doctor = Docprofile.objects.get(user=request.staff)
#     except Docprofile.DoesNotExist:
#         # Handle the case where a 'Docs' object does not exist for the logged-in user
#         # You can redirect or display an error message as needed
#         return render(request, 'error_template.html', {'error_message': 'Doctor profile not found'})

#     # Extract the doctor's name from the 'Name' attribute of the 'Docs' object
#     doctor_name = logged_in_doctor.doctor_name

#     if request.method == 'POST':
#         # Retrieve form data from POST request
#         date = request.POST.get('date')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')

#         if start_time:
#             # Create and save the time slot associated with the logged-in doctor
#             doctor = logged_in_doctor  # Use the 'logged_in_doctor' from your previous code
#             Timeslot = Timeslot(doctor=doctor, date=date, start_time=start_time, end_time=end_time)
#             Timeslot.save()

#             # Optionally, you can add a success message or redirect to another page
#             return render(request, 'timeslot.html', {'doctor_name': doctor_name, 'success_message': 'Time slot saved successfully'})
#         else:
#             # Handle the case where 'start_time' is not provided
#             # You can render an error message or take appropriate action
#             return render(request, 'timeslot.html', {'doctor_name': doctor_name, 'error_message': 'Please provide a valid start time'})

#     # Render the template for both GET and POST requests
#     return render(request, 'timeslot.html', {'doctor_name': doctor_name})


# @login_required
# def doctor_timeslots(request):
#     # Get the logged-in doctor
#     logged_in_doctor = Docprofile.objects.get(user=request.staff)

#     # Fetch time slots associated with the logged-in doctor
#     time_slots = Timeslot.objects.filter(doctor=logged_in_doctor)

#     return render(request, 'timeslotdisplay.html', {'time_slots': time_slots})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import  Docprofile  # Import Docprofile model
from datetime import datetime


# @login_required
# def add_time_slot(request):
#     if request.method == 'POST':
#         # Get user from the request (you may need to adjust this depending on your authentication system)
#         user = request.user  # Assuming you have authentication and the user is logged in
#         # doctor_name = user.Docprofile.name
#         # Get data from the form
#         date = request.POST.get('date')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
        
#         # Create a new Timeslot object and save it
#         timeslot = Timeslot(user=user, date=date, start_time=start_time, end_time=end_time)
#         timeslot.save()
        
#         # Optionally, you can add a success message
#         messages.success(request, 'Time slot added successfully')
        
#         # Redirect to a different page or template
#         return redirect('view_timeslots')  # Replace 'some_success_page' with the actual URL name or path
        
#     return render(request, 'doctors/timeslot.html')





def deactivate_user(request, user_id):
    # Get the user by ID or return a 404 error if not found
    user = get_object_or_404(User, id=user_id)
    
    # Check if the user is not already inactive
    if user.is_active:
        # Deactivate the user
        user.is_active = False
        user.save()
    
    # Redirect back to the user list or a different page as needed
    return redirect('admins_registereduser')  # Change to your desired URL name

def activate_user(request, user_id):
    # Get the user by ID or return a 404 error if not found
    user = get_object_or_404(User, id=user_id)
    
    # Check if the user is not already active
    if not user.is_active:
        # Activate the user
        user.is_active = True
        user.save()
    
    # Redirect back to the user list or a different page as needed
    return redirect('admins_registereduser') 
     


import logging

logger = logging.getLogger(__name__)
def count_view(request):
    # Count the number of doctors and patients
    

    doctors_count = Docprofile.objects.count()
    patients_count = UserProfile.objects.count()
    # Log the counts for debugging
    logger.debug(f"Doctors Count: {doctors_count}")
    logger.debug(f"Patients Count: {patients_count}")
    # Pass the counts as context variables to the template
    context = {
        'doctors_count': doctors_count,
        'patients_count': patients_count,
    }
    return render(request, 'admins_index.html', context)

from django.shortcuts import render
from .models import Slots, Docprofile,Appointments

from django.contrib.auth.decorators import login_required

@login_required
# 

# def get_dates(request, doctor_id):
#     try:
#         # Fetch dates for the selected doctor (doctor_id) from your database
#         # Replace the following line with your actual database query logic
        
#         dates = Slots.objects.filter(doctor_id=doctor_id).values_list('date', flat=True).distinct()
        
#         # Construct a list of date options in HTML format
#         date_options = ["<option value='{0}'>{0}</option>".format(date.strftime('%Y-%m-%d')) for date in dates]
#     except Slots.DoesNotExist:
#         # Handle the case where no slots are found for the selected doctor
#         date_options = []

#     return JsonResponse({"date_options": date_options})


# def get_times(request, doctor_id, selected_date):
#     # Your view logic here

#     try:
#         # Fetch all time slots for the selected doctor (doctor_id) and date (selected_date) from your database
#         all_time_slots = Slots.objects.filter(doctor_id=doctor_id, date=selected_date)

#         # Fetch the time slots that are already booked as appointments
#         booked_time_slots = Appointment.objects.filter(doctor_id=doctor_id, date=selected_date).values_list('slot__id', flat=True)

#         # Filter out the free time slots by excluding the booked ones
#         free_time_slots = all_time_slots.exclude(id__in=booked_time_slots)

#         # Construct a list of free time slot options in HTML format
#         time_options = [
#             {
#                 "id": slot.id,
#                 "text": f"{slot.start_time.strftime('%I:%M %p')} - {slot.end_time.strftime('%I:%M %p')}"
#             }
#             for slot in free_time_slots
#         ]
#     except Slots.DoesNotExist:
#         # Handle the case where no slots are found for the selected doctor and date
#         time_options = []

#     return JsonResponse({"time_options": time_options})

# def dr_timeslots(request):
#     # Check if a 'Docs' object exists for the logged-in user
#     try:
#         logged_in_doctor = Docprofile.objects.get(user=request.user)
#     except Docs.DoesNotExist:
#         # Handle the case where a 'Docs' object does not exist for the logged-in user
#         # You can redirect or display an error message as needed
#         # return render(request, 'error_template.html', {'error_message': 'Doctor profile not found'})
#         print("Doctor Profile Doesnt exist")
#     # Extract the doctor's name from the 'Name' attribute of the 'Docs' object
#     doctor_name = logged_in_doctor.name

#     if request.method == 'POST':
#         # Retrieve form data from POST request
#         date = request.POST.get('date')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')

#         if start_time:
#             doctor = logged_in_doctor  # Use the 'logged_in_doctor' from your previous code
#             slot = Slots(doctor=doctor, date=date, start_time=start_time, end_time=end_time)
#             slot.save()

#             # Optionally, you can add a success message or redirect to another page
#             return redirect('dr_timeslots_shows')  
#         else:
#             # Handle the case where 'start_time' is not provided
#             # You can render an error message or take appropriate action
#             return render(request, 'doctors/timeslot.html', {'doctor_name': doctor_name, 'error_message': 'Please provide a valid start time'})

#     # Render the template for both GET and POST requests
#     return render(request, 'doctors/timeslot.html', {'doctor_name': doctor_name})



def admins_bookscreening(request):
 
     return render(request, 'admins/screeningtimeslot.html')
    

def bookscreening(request):
    if request.method == 'POST':
        # Retrieve form data from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        comments = request.POST.get('comments')

        # Create and save the form data to the database
        form_data = FormData(
            name=name,
            email=email,
            age=age,
            gender=gender,
            comments=comments
        )
        form_data.save()

        # Redirect to a success page or perform other actions
        return redirect('bookscreening.html')  # Replace 'success_page' with your success URL
    
    return render(request,'bookscreening.html')



@login_required
def dr_timeslots_shows(request):
    # Get the logged-in doctor
    logged_in_doctor = Docprofile.objects.get(user=request.user)

    # Fetch time slots associated with the logged-in doctor
    time_slots = Slots.objects.filter(doctor=logged_in_doctor)
    print(time_slots)
    return render(request, 'doctors/timeslotdisplay.html', {'time_slots': time_slots})


import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.contrib.auth.models import User  # Import the user model you are using

 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
from django.shortcuts import render
from django.conf import settings
from razorpay import Client as RazorpayClient
from .models import Appointments, Payment


def payment_confirm(request):
    # Retrieve the appointment instance
    
    currency = 'INR'
    amount = int(200*100)  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(
        amount=amount,
        currency=currency,
        payment_capture='0'
    ))

    # order id of the newly created order
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'

    # Create a Payment for the appointment
    payment = Payment.objects.create(
        user=request.user,
        payment_amount=amount,  # Specify the payment amount
        payment_status='Pending',  # Set payment status to "Pending"
    )

    # Render the success template with the necessary context
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url
    }

    return render(request, 'payment_confirm.html', context=context)


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            # Get the payment details from the POST request
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            amount=request.POST.get('razorpay_amount', '')

            # Verify the payment signature
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,

            }
            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result is not None:
                amount = int(200*100)  # Rs. 200

                # Capture the payment
                razorpay_client.payment.capture(payment_id, amount)

                # Save payment details to the Payment model
                # Assuming you have a Payment model defined
                payment = Payment.objects.create(
                    user=request.user,  # Assuming you have a logged-in user
                    payment_amount=amount/100,
                    payment_status='Success',  # Assuming payment is successful
                )

                # Redirect to a success page with payment details
                return redirect('paymentsuccess')  # Replace 'orders' with your actual success page name or URL
            else:
                # Signature verification failed
                return HttpResponse("Payment signature verification failed", status=400)
        except Exception as e:
            # Handle exceptions gracefully
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
    else:
        # Handle non-POST requests
        return HttpResponse("Invalid request method", status=405)
def paymentsuccess(request):
    # Perform any necessary actions, such as updating the payment status in your database
    # You may also retrieve specific payment-related data and user information here
    
    return render(request, 'paymentsuccess.html')





def delete_specialization(request, specialization_id):
    # Retrieve the specialization object from the database or return a 404 error if it doesn't exist
    specialization = get_object_or_404(Specialization, id=specialization_id)
    specialization.status = True
    specialization.save()
    messages.success(request, 'Specialization deleted successfully.')
    return redirect('admins_specialities')  


def display_booked_appointments(request):
    bookeddoctor = Docprofile.objects.filter(user = request.user)
    booked_appointments = Appointment.objects.filter(doctor = bookeddoctor)
   

    context = {
        'booked_appointments': booked_appointments,
    }

    return render(request, 'doctors/appointments.html', context)
from .models import LeaveApplication

@login_required
def doctors_leave(request):
    # Fetch all leave applications
    leave_applications = LeaveApplication.objects.all()

    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')
        
        # Create a new LeaveApplication instance
        leave_application = LeaveApplication.objects.create(
            doctor=request.user,
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            reason=reason
        )
        
        # Send notification or perform any other actions here
        
        messages.success(request, 'Leave application submitted successfully.')
        return redirect('doctors_leavesubmit')  # Redirect to the leavesubmit page after submission
        
    else:
        # Check if the user has submitted a leave application
        leave_application_exists = LeaveApplication.objects.filter(doctor=request.user).exists()
        if leave_application_exists:
            return redirect('doctors_leavesubmit')
        else:
            return render(request, 'doctors/leave.html', {'leave_applications': leave_applications})



def doctors_leavesubmit(request):
    # Check if the user has submitted a leave application
    leave_application_exists = LeaveApplication.objects.filter(doctor=request.user).exists()
    print("Leave Application Exists:", leave_application_exists)  # Add this line for debugging
    if leave_application_exists:
        return render(request, 'doctors/leavesubmit.html')
    else:
        print("Redirecting to doctors_leave")  # Add this line for debugging
        # Redirect to the leave application page if no application exists
        return redirect('doctors_leave')

def admins_leave(request):
    
    pending_leave_applications = LeaveApplication.objects.filter(status='pending')
    print(pending_leave_applications)
    return render(request, 'admins/leaveapprove.html', {'leave_applications': pending_leave_applications})
    
def admin_view_leave_applications(request):
    # Fetch pending leave applications
    pending_leave_applications = LeaveApplication.objects.filter(status='pending')
    print(pending_leave_applications)
    return render(request, 'admins/leaveapprove.html', {'leave_applications': pending_leave_applications})

def approve_leave(request, leave_id):
    # Retrieve the leave application object
    leave_application = LeaveApplication.objects.get(id=leave_id)
    
    # Update the status to 'approved'
    leave_application.status = 'approved'
    leave_application.save()
    
    # Redirect back to the leave approval page
    return redirect('admins_leave')

def reject_leave(request, leave_id):
    # Retrieve the leave application object
    leave_application = LeaveApplication.objects.get(id=leave_id)
    
    # Update the status to 'rejected'
    leave_application.status = 'rejected'
    leave_application.save()
    
    # Redirect back to the leave approval page
    return redirect('admins_leave')
from .models import Blog
def admins_addblog(request):

    if request.method == 'POST':
    
        title = request.POST['title']
        content = request.POST['content']
        blog_date = request.POST['blog_date']
        images = request.FILES.get('images')
        
        print(images)
        # Handle image upload if needed
        
        # Create a new Blog instance
        new_blog = Blog(
            title=title,
            content=content,
            blog_date=blog_date,
            images=images
        )
        
        # Save the new blog entry
        new_blog.save()
        
        return redirect('admins_viewblog')  # Redirect to a list view of all blogs

    return render(request, 'admins/addblog.html')
def admins_viewblog(request):
    
    blogs = Blog.objects.all()
    return render(request, 'admins/viewblog.html', {'blogs': blogs})




def showmore_view(request):
    doctors = Docprofile.objects.all()
    
    
    return render(request, 'patient/showmore.html', {'doctors': doctors})




# def get_new_references_count(request):
#     new_references_count = ReferPatient.objects.filter(is_new=True).count()
#     return JsonResponse({'count': new_references_count})

def accept_patient(request, patient_id):
    refer_patient = ReferPatient.objects.get(id=patient_id)
    refer_patient.accept = True
    refer_patient.is_new = False  # Mark as not new after accept action
    refer_patient.save()
    return redirect('refer_patient')

def decline_patient(request, patient_id):
    refer_patient = ReferPatient.objects.get(id=patient_id)
    refer_patient.decline = True
    refer_patient.is_new = False  # Mark as not new after decline action
    refer_patient.save()
    return redirect('refer_patient')

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

from django.core.mail import send_mail
from django.conf import settings

# def patientreferences(request):
#     if request.method == 'POST':
#         patient_id = request.POST.get('patient_id')
#         patient = get_object_or_404(ReferPatient, id=patient_id)
        
#         # Set accept status to True
#         patient.accept = True
#         patient.save()

#         # Get referral doctor's email and other details from ReferPatient
#         referring_doctor_email = patient.referring_doctor_email
#         referring_doctor_name = patient.referring_doctor.name
        
#         # Send email to the referring doctor
#         subject = 'Patient Accepted'
#         message = f'Hi {referring_doctor_name},\n\nThis is to inform you that the patient has been accepted.'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [referring_doctor_email]
#         send_mail(subject, message, from_email, recipient_list)
        
#         return redirect('patientreferences')  # Redirect to some URL after accepting patient
    
#     referring_doctor = request.user.docprofile
#     referred_patients = ReferPatient.objects.filter(referring_doctor=referring_doctor)
#     return render(request, 'doctors/patientreferences.html', {'referred_patients': referred_patients})


logger = logging.getLogger(__name__)

# def patientreferences(request):
#     if request.method == 'POST':
#         patient_id = request.POST.get('patient_id')
#         patient = get_object_or_404(ReferPatient, id=patient_id)
        
#         # Set accept status to True
#         patient.accept = True
#         patient.save()

#         # Get referral doctor's email and other details from ReferPatient
#         referring_doctor_email = patient.referring_doctor_email
#         referring_doctor_name = patient.referring_doctor.name
        
#         # Send email to the referring doctor
#         subject = 'Patient Accepted'
#         message = f'Hi {referring_doctor_name},\n\nThis is to inform you that the patient has been accepted.'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [referring_doctor_email]
        
#         try:
#             # Attempt to send the email
#             num_emails_sent = send_mail(subject, message, from_email, recipient_list)
#             if num_emails_sent == 1:
#                 # Print confirmation that the email has been sent successfully to the console
#                 print(f"Email sent successfully to {referring_doctor_email}")
#             else:
#                 # Print an error message to the console if the email sending fails
#                 print(f"Failed to send email to {referring_doctor_email}")
#         except Exception as e:
#             # Print any exceptions that occur during the email sending process to the console
#             print(f"An error occurred while sending email to {referring_doctor_email}: {e}")
        
#         return redirect('patientreferences')  # Redirect to some URL after accepting patient
    
#     referring_doctor = request.user.docprofile
#     referred_patients = ReferPatient.objects.filter(referring_doctor=referring_doctor)
#     return render(request, 'doctors/patientreferences.html', {'referred_patients': referred_patients})
from .models import ReferPatient
def refer_patient(request):
    doctors= Docprofile.objects.all()

    if request.method == 'POST':
        # Extract data from the POST request
        hospital_name = request.POST.get('hospital_name')
        patient_name = request.POST.get('patient_name')
        referring_doctor_id = request.POST.get('referring_doctor')
        referring_doctor_name= request.POST.get('referring_doctor_name')
        referring_doctor_email= request.POST.get('referring_doctor_email')
        case_sheet= request.FILES.get('case_sheet')
        comments= request.POST.get('comments')

        # print(referring_doctor_id)
        medical_details = request.FILES.get('medical_details')
        
        # Assuming 'referring_doctor_id' is the ID of the selected doctor
        if hospital_name and patient_name and referring_doctor_id:
            try:
                referring_doctor = Docprofile.objects.get(id=referring_doctor_id)
                print("Hello",referring_doctor)
                # Create a new ReferPatient object and save it
                refer_patient = ReferPatient.objects.create(
                    hospital_name=hospital_name,
                    patient_name=patient_name,
                    referring_doctor=referring_doctor,
                    referring_doctor_name=referring_doctor_name,
                    referring_doctor_email=referring_doctor_email,
                    case_sheet=case_sheet,
                    comments=comments,
                    medical_details=medical_details
                )
                return redirect('refer_patient')  # Redirect after saving
            except (ValueError, Docprofile.DoesNotExist):
                # Handle invalid doctor ID or other errors
                pass
    
    return render(request, 'referpatient.html',{'doctors' : doctors})
    
   

def patientreferences(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        action = request.POST.get('action')  # Accept or Decline
        
        patient = get_object_or_404(ReferPatient, id=patient_id)
        
        # Set accept or decline status
        if action == 'accept':
            patient.accept = True
            patient.decline = False  # Ensure that the opposite action is reset
            message = 'Hi Dr.{},\n\nThis is to inform you that the patient has been accepted.'.format(patient.referring_doctor_name)
        elif action == 'decline':
            patient.accept = False
            patient.decline = True
       
             # Ensure that the opposite action is reset
            message = 'Hii{},\n\nThis is to inform you that the patient has been declined.'.format(patient.referring_doctor_name)
        else:
            return redirect('patientreferences')  # or handle invalid action
        
        patient.save()
        
        # Send email to the referring doctor
        subject = 'Patient Status Update'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [patient.referring_doctor_email]
        send_mail(subject, message, from_email, recipient_list)

        # Context for rendering the template
        referring_doctor = request.user.docprofile
        referred_patients = ReferPatient.objects.filter(referring_doctor=referring_doctor)
        context = {'referred_patients': referred_patients}

        # Adding email sent flag to the context
        context['email_sent'] = True

        return render(request, 'doctors/patientreferences.html', context)
    
    referring_doctor = request.user.docprofile
    referred_patients = ReferPatient.objects.filter(referring_doctor=referring_doctor)
    return render(request, 'doctors/patientreferences.html', {'referred_patients': referred_patients})

def confirm_appointment(request):
    return render(request, 'confirmapp.html')

def book_appointment(request):
    doctors = Docprofile.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        appointment_type = request.POST.get('appointmentType')
        reason = request.POST.get('reason')
        doctor_id = request.POST.get('doctor')
        appointment_time = request.POST.get('apptime')
        appointment_date = request.POST.get('appdate')
        
        # Check if all required fields are provided
        if name and age and email and appointment_type and doctor_id and appointment_time and appointment_date:
            try:
                # Retrieve the UserProfile instance by name
                user_profile = UserProfile.objects.get(name=name)
            except UserProfile.DoesNotExist:
                # If the user does not exist, display an error message and redirect back to the form
                messages.error(request, 'User with provided name does not exist!')
                return redirect('book_appointment')            # Create a new DoctorAppointment object and save it to the database
            appointment = Appointments(
                name=user_profile,
                age=age,
                email=email,
                appointment_type=appointment_type,
                reason=reason,
                doctor_id=doctor_id,
                appointment_time=appointment_time,
                appointment_date=appointment_date
            )
            appointment.save()
            
            messages.success(request, 'Appointment booked successfully!')
            return redirect('payment_confirm')  # Redirect to a success page
            
        else:
            messages.error(request, 'Please fill out all required fields!')
            return redirect('book_appointment')  # Redirect back to the appointment booking form
    
    # If the request method is not POST, render the form template
    return render(request, 'patient/bookappointment.html',{'doctors': doctors})

# def patient_bookappointment(request):
#     # userprofile = request.user.UserProfile
#     doctors = Docprofile.objects.all()

#     print(doctors)
#     if request.method == 'POST':
#         name = request.POST.get('fullName')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone')
#         doctor_id = request.POST.get('doctor')
#         symptoms = request.POST.get('symptoms')
#         appdate = request.POST.get('appdate')
#         apptime = request.POST.get('apptime')
        
#         try:
#             doctor = Docprofile.objects.get(id=doctor_id)
#             user = User.objects.get(id=request.user.id)

#             existing_appointment = Appointment.objects.filter(
#                 doctor=doctor,
#                 app_date=appdate,
#                 app_time=apptime
#             ).first()

#             if existing_appointment:
#                 error_message = 'Appointment slot is already booked'
#                 return render(request, 'patient/bookappointment.html', {'error_message': error_message, 'doctors': doctors})

#             appointment = Appointment(
#                 fullName=name,
#                 age=age,
#                 gender=gender,
#                 phone=phone,
#                 email=email,
#                 doctor=doctor,
#                 user=user,
#                 app_date=appdate,
#                 app_time=apptime,
#             )
#             appointment.save()
#             return redirect('payment_confirm')  # Redirect to a success page

#         except ValueError:
#             # Handle the case where the selected_time_slot is in an invalid format
#             return render(request, 'patient/bookappointment.html', {'error_message': 'Invalid time format'})

#     return render(request, 'patient/bookappointment.html', {'doctors': doctors})


