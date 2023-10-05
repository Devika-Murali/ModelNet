"""
URL configuration for modelnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from doctor import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home, name='Home5'),
    path('admin/', admin.site.urls),
    path('Home/',views.Home,name='Home'),
    path('About/',views.About,name='About'),
    path('basepatient/',views.basepatient,name='basepatient'),
    path('bookscreening/',views.bookscreening,name='bookscreening'),

    path('doctors_basedoctor/',views.doctors_basedoctor,name='doctors_basedoctor'),
    path('mypatients/',views.mypatients,name='mypatients'),
    path('patientprofile/',views.profile,name='patientprofile'),
    path('profileset/',views.profileset,name='profileset'),
    path('admins_index/', views.admins_index, name='admins_index'),
    path('admins_patientlist/', views.admins_patientlist, name='admins_patientlist'),
    path('admins_appointmentlist/', views.admins_appointmentlist, name='admins_appointmentlist'),
    path('admins_specialities', views.specializations, name='admins_specialities'),
    path('admins_registereduser', views.admins_registereduser, name='admins_registereduser'), 
    path('admins_dashlegal', views.dashlegal, name='admins_dashlegal'),
    path('patientappointment/',views.patientappointment,name='patientappointment'),
    path('patientbooking/',views.patientbooking,name='patientbooking'),
    path('patientprofileset/',views.patientprofileset,name='patientprofileset'),
    path('profileset',views.DoctorProfileView,name='profileset'),
    path('admins_doctorlist/',views.admins_doctorlist,name='admins_doctorlist'),
    path('patient_bookappointment/', views.patient_bookappointment, name='patient_bookappointment'), 
    path('patient_medicalhistory/', views.patient_medicalhistory, name='patient_medicalhistory'),  
    path('doctors_appointments/',views.doctors_appointments,name='doctors_appointments'),
    path('doctors_timeslot/',views.doctors_timeslot,name='doctors_timeslot'),
    path('doctors_timeslotdisplay/',views.doctors_timeslotdisplay,name='doctors_timeslotdisplay'),
    path('doctors_testresult/',views.doctors_testresult,name='doctors_testresult'),

    path('Doctor_patienthistory/',views.Doctor_patienthistory,name='Doctor_patienthistory'),
    path('delete_specialization/', views.delete_specialization, name='delete_specialization'),

    path('scheduletiming/',views.scheduletiming,name='scheduletiming'),
    path('testresult/',views.testresult,name='testresult'),
    path('doctor_profile/', views.DoctorProfileView, name='Doctor_profile'),
    path('register/',views.register, name='register'),
    path('DoctorReg/',views.DoctorReg, name='DoctorReg'),
    path('login_page/',views.login_page,  name='login_page'),
    path('accounts/', include('allauth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.loggout, name='loggout'),
    path('profile', views.profile, name='profile'),
    path('adddoctor/', views.adddoctor, name='adddoctor'),
    path('edituser/<int:user_id>/', views.edituser, name='edituser'),
    path('approve_certification/<int:certification_id>/', views.approve_certification, name='approve_certification'),
    path('reject_certification/<int:certification_id>/', views.reject_certification, name='reject_certification'),
    
    path('editrecords/<int:patient_id>/', views.submit_medical_history, name='editrecords'),

    path('finddoctor/', views.patient_finddoctor, name='finddoctor'),
   

    path('edit_specialization/<int:specialization_id>/', views.edit_specialization, name='edit_specialization'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    path('add_time_slot/', views.add_time_slot, name='add_time_slot'),
    path('view_timeslots/', views.view_timeslots, name='view_timeslots'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('get_dates_for_doctor/', views.get_dates_for_doctor, name='get_dates_for_doctor'),

    # URL for getting time slots based on selected Ashaworker and date
    path('get_timeslots_for_date/', views.get_timeslots_for_date, name='get_timeslots_for_date'),
    # URL for the get_available_dates view to handle AJAX requests
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('count/', views.count_view, name='count_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)