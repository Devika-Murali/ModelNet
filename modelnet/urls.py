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
from django.contrib.auth.decorators import login_required
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
    path('profileset/',views.profileset,name='profileset'),
    path('admins_index/', views.admins_index, name='admins_index'),
    path('admins_patientlist/', views.admins_patientlist, name='admins_patientlist'),
    path('admins_appointmentlist/', views.admins_appointmentlist, name='admins_appointmentlist'),
    path('admins_specialities', views.specializations, name='admins_specialities'),
    path('admins_registereduser', views.admins_registereduser, name='admins_registereduser'), 
    path('admins_dashlegal', views.dashlegal, name='admins_dashlegal'),
    path('admins_bookscreening', views.admins_bookscreening, name='admins_bookscreening'), 
    path('admins_addblog/', views.admins_addblog, name='admins_addblog'),
    path('admins_viewblog/', views.admins_viewblog, name='admins_viewblog'),

    path('admins_leave/', views.admins_leave, name='admins_leave'),
    path('admin_view_leave_applications', views.admin_view_leave_applications, name='admin_view_leave_applications'),


    path('patientappointment/',views.patientappointment,name='patientappointment'),
    path('patientbooking/',views.patientbooking,name='patientbooking'),
    path('patientprofileset/',views.profile,name='patientprofileset'),
    path('profileset',views.DoctorProfileView,name='profileset'),
    path('admins_doctorlist/',views.admins_doctorlist,name='admins_doctorlist'), 
    path('patient_medicalhistory/', views.patient_medicalhistory, name='patient_medicalhistory'),  
    path('doctors_appointments/',views.doctors_appointments,name='doctors_appointments'),
    path('doctors_leave/',views.doctors_leave,name='doctors_leave'),
    path('doctors_leavesubmit/',views.doctors_leavesubmit,name='doctors_leavesubmit'),

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
    path('adddoctor/', views.adddoctor, name='adddoctor'),
    path('edituser/<int:user_id>/', views.edituser, name='edituser'),
    path('approve_certification/<int:certification_id>/', views.approve_certification, name='approve_certification'),
    path('reject_certification/<int:certification_id>/', views.reject_certification, name='reject_certification'),
    
    path('editrecords/<int:patient_id>/', views.submit_medical_history, name='editrecords'),
    path('finddoctor/', views.patient_finddoctor, name='finddoctor'),
    path('edit_specialization/<int:specialization_id>/', views.edit_specialization, name='edit_specialization'),
    path('delete_specialization/<int:specialization_id>/', views.delete_specialization, name='delete_specialization'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    # URL for getting time slots based on selected Ashaworker and date
    # URL for the get_available_dates view to handle AJAX requests
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('count/', views.count_view, name='count_view'),
    path('dr_timeslots',views.dr_timeslots,name="dr_timeslots"),
    path('dr_timeslots_shows',views.dr_timeslots_shows, name= 'dr_timeslots_shows'),
    path('get_dates/<int:doctor_id>/', views.get_dates, name='get_dates'),
    path('get_times/<int:doctor_id>/<str:selected_date>/', views.get_times, name='get_times'),
    path('patient_bookappointment/', views.patient_bookappointment, name='patient_bookappointment'),
    path('paymentsuccess/', views.paymentsuccess, name='paymentsuccess'),
    path('appointments/', views.display_booked_appointments, name='appointments'),
    path('payment_confirm/', views.payment_confirm, name='payment_confirm'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('doctor-profile/', views.doctor_profile_details, name='doctor_profile_details'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)