from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout,get_user_model
from .models import UserProfile,Docprofile,Specialization,Certification,Timeslot
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from .models import PatientInfo 
from .models import Specialization
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
    return render(request,'Home.html')
def About(request):
    return render(request,'About.html')  
def basepatient(request):
    return render(request,'basepatient.html')
def bookscreening(request):
    return render(request,'bookscreening.html')
def doctors_basedoctor(request):

    existing_certification = Certification.objects.filter(user=request.user).first()

    if existing_certification:
        return render(request, 'doctors/basedoctor.html', {'existing_certification': existing_certification})

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

    return render(request,'doctors_basedoctor.html') 
def doctors_timeslot(request):
    return render(request,'doctors/timeslot.html')
def doctors_changepass(request):
    return render(request,'doctors/changepass.html')  
def doctors_testresult(request):
    return render(request,'doctors/testresult.html')
def doctors_timeslotdisplay(request):
    return render(request,'doctors/timeslotdisplay.html') 
def testresult(request):
    return render(request,'testresult.html') 
def doctors_appointments(request):
    return render(request,'doctors/appointments.html')  
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
def admins_patientlist(request):
    # Retrieve the list of patients (users) from the database
    patients = User.objects.filter(is_superuser=False, is_staff=False)

    # Pass the list of patients to the template
    return render(request, 'admins/patientlist.html', {'users': patients})
# def patient_bookappointment(request):
#     return render(request, 'patient/bookappointment.html')
def admins_appointmentlist(request):
    return render(request, 'admins/appointmentlist.html')


def patient_medicalhistory(request):
    current_user = request.user
    patient_info = PatientInfo.objects.get(user=current_user)

    # Pass the patient_info object to the template context
    context = {
        'patient_info': patient_info,
    }
    return render(request, 'patient/medicalhistory.html',context)
def patient_finddoctor(request):
    return render(request, 'patient/finddoctor.html')
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
                messages.info(request, "Registered Succesfully")
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
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                category = Specialization.objects.get(id=select_category_id)
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
    return redirect('Home')


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

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
        
        # Retrieve profile picture and medical history files
        profile_pic = request.FILES.get('profile_pic')
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
        user_profile.country = country
        user_profile.blood_group = blood_group
        user_profile.gender = gender

        # Handle profile picture and medical history files
        if profile_pic:
            user_profile.profile_pic = profile_pic
        if medical_history:
            user_profile.medical_history = medical_history

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
        docprofile = Docprofile(user=request.user)
        docprofile.save()
        return redirect('profileset') 


    context = {
        'doc_profile': doc_profile
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
    specializations = Specialization.objects.all()
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
    print(patient_id)
    patient = UserProfile.objects.get(pk=patient_id)
    
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
        patient_info = PatientInfo(
           # Associate the data with the patient identified by patient_id
            user =patient.user,
            diagnosis_date=diagnosis_date,
            cancer_stage=cancer_stage,
            biopsy_results=biopsy_results,
            oncologist_name=oncologist_name,
            allergy_name=allergy_name,
            allergy_severity=allergy_severity,
            medication_name=medication_name,
            dosage=dosage,
            frequency=frequency,
            start_date=start_date
        )
        patient_info.save()
        patient.save()
        # Redirect to the 'editrecords' URL after successful submission
        return redirect('mypatients')

    # Handle GET request or invalid submissions here
    return render(request, 'doctors/editrecords.html')
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
from .models import Timeslot, Docprofile  # Import Docprofile model

@login_required
def add_time_slot(request):
    try:
        # Attempt to get the Docprofile associated with the logged-in user
        doctor_profile = request.user.docprofile  # Note lowercase "docprofile"

        if request.method == 'POST':
            date = request.POST['date']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']

            try:
                # Create a new Timeslot associated with the doctor's profile
                Timeslot.objects.create(
                    doctor_name=doctor_profile,
                    date=date,
                    start_time=start_time,
                    end_time=end_time
                )
                messages.success(request, 'Time slot added successfully!')
            except Exception as e:
                messages.error(request, f'Error: {e}')
    except Docprofile.DoesNotExist:
        # Handle the case where there is no Docprofile associated with the user
        messages.error(request, 'No Docprofile associated with your account. Please create one.')

    return redirect('view_timeslots')



from django.shortcuts import render
from .models import Timeslot, Docprofile
from django.contrib.auth.decorators import login_required

@login_required
def view_timeslots(request):
    doctor_name = request.user.docprofile

    # Retrieve timeslots for the specific doctor
    timeslots = Timeslot.objects.filter(doctor_name=doctor_name)

    context = {
        'doctor_name': doctor_name,
        'timeslots': timeslots,
    }

    return render(request, 'doctors/timeslotdisplay.html', context)

def book_appointment(request, appointment_id=None):
    userprofile = request.user.UserProfile
    doctors = Docprofile.objects.all()

    if request.method == 'POST':
        name = request.POST.get('fullName')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        doctor = request.POST.get('doctor')
        date_id = request.POST.get('appointmentDate')
        selected_time_slot = request.POST.get('appointmentTime')

        try:
            slot = Timeslot.objects.get(id=selected_time_slot)
            doctor = Docprofile.objects.get(id=doctor_id)
            user = user.objects.get(id=request.user.id)

            appointment = Appointment(
                name=name,
                age=age,
                gender=gender,
                phone=phone,
                email=email,
                doctor=doctor,
                user=user,
                slot=slot,
                date=date_id,
                
            )
            appointment.save()
            return redirect('basedoctor')  # Redirect to a success page

        except Timeslot.DoesNotExist:
            # Handle the case where the selected time slot does not exist
            return render(request, 'bookappointment.html', {'error_message': 'Time slot not found'})
        except ValueError:
            # Handle the case where the selected_time_slot is in an invalid format
            return render(request, 'bookappointment.html', {'error_message': 'Invalid time format'})

    return render(request, 'bookappointment.html', {'doctors': doctors,'userprofile': userprofile,'appointment_id': appointment_id})

        

def get_dates_for_doctor(request):
    doctor_id = request.GET.get('doctor_id')
    try:
        doctor = Docprofile.objects.get(id=doctor_id)
        slots = Timeslot.objects.filter(doctor=doctor)
        date_options = [slot.date.strftime('%Y-%m-%d') for slot in slots]
        return JsonResponse({'date_options': date_options})
    except Docprofile.DoesNotExist:
        return JsonResponse({'error_message': 'Doctor not found'})

@login_required
def get_timeslots_for_date(request):
    doctor_id = request.GET.get('doctor_id')
    selected_date = request.GET.get('selected_date')

    try:
        doctor = Docprofile.objects.get(id=doctor_id)
        slots = Timeslot.objects.filter(doctor=doctor, date=selected_date)
        time_options = [{'id': slot.id, 'text': f'{slot.start_time.strftime("%I:%M %p")} - {slot.end_time.strftime("%I:%M %p")}'}
                        for slot in slots]
        return JsonResponse({'time_options': time_options})
    except Docprofile.DoesNotExist:
        return JsonResponse({'error_message': 'Doctor not found'})



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
     

#  patient/ bookapponment
from django.shortcuts import render
from .models import Docprofile, Timeslot

def patient_bookappointment(request):
    # Retrieve a list of doctors from the Docprofile model
    doctors = Docprofile.objects.all()

    # Retrieve a list of available dates from the Timeslot model
    date_options = Timeslot.objects.values_list('date', flat=True).distinct()

    # Retrieve a list of available time slots
    time_options = Timeslot.objects.all()

    context = {
        'doctors': doctors,
        'date_options': date_options,
        'time_options': time_options,
    }

    return render(request, 'patient/bookappointment.html', context)
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