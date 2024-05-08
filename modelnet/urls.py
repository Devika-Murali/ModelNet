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
from doctor.views import patientreferences
urlpatterns = [
    path('',views.Home, name='Home5'),
    path('admin/', admin.site.urls),
    # path('Home/',views.Home,name='Home'),
    path('About/',views.About,name='About'),
    path('basepatient/',views.basepatient,name='basepatient'),
    path('bookscreening/',views.bookscreening,name='bookscreening'),
    path('donation/', views.donation, name='donation'),
    path('donationpay/', views.donation_payment, name='donation_payment'),
    path('patientreferences/<int:doc_id>', views.patientreferences, name='patientreferences'),
    path('accept-patient/<int:patient_id>/',views.accept_patient, name='accept_patient'),
    path('decline-patient/<int:patient_id>/', views.decline_patient, name='decline_patient'),
    path('doctors_basedoctor/',views.doctors_basedoctor,name='doctors_basedoctor'),
    path('mypatients/<int:doc_id>',views.mypatients,name='mypatients'),
    path('profileset/<int:doc_id>',views.profileset,name='profileset'),
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
    path('admins/donations/', views.admins_donations, name='admins_donations'),
    path('patientappointment/',views.patientappointment,name='patientappointment'),
    path('patientbooking/',views.patientbooking,name='patientbooking'),
    path('patientprofileset/',views.profile,name='patientprofileset'),
    path('profileset/<int:doc_id>',views.DoctorProfileView,name='profileset'),
    path('admins_doctorlist/',views.admins_doctorlist,name='admins_doctorlist'), 
    path('patient_medicalhistory/', views.patient_medicalhistory, name='patient_medicalhistory'),  
    path('doctors_leave/<int:doc_id>',views.doctors_leave,name='doctors_leave'),
    # path('doctors_leavesubmit/',views.doctors_leavesubmit,name='doctors_leavesubmit'),
    path('view_leave_requests/', views.view_leave_requests, name='view_leave_requests'),
    path('doctors_testresult/',views.doctors_testresult,name='doctors_testresult'),
    path('leave-history/', views.doctors_leavehistory, name='doctors_leavehistory'),
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
    path('doctors_patienthistory/<int:patient_id>/', views.doctors_patienthistory, name='doctors_patienthistory'),
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
    # path('payment/', views.payment, name='payment'),
    path('paymentsuccess/', views.paymentsuccess, name='paymentsuccess'),
    path('payment_confirm/', views.payment_confirm, name='payment_confirm'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('paymenthandler_donation/', views.paymenthandler_donation, name='paymenthandler_donation'),

    path('showmore/<int:doctor_id>/', views.showmore_view, name='showmore'), 
    path('referpatient/', views.refer_patient, name='refer_patient'),
    path('confirm-appointment/', views.confirm_appointment, name='confirm_appointment'),
    path('book-appointment/<int:doc_id>/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.Appointments, name='appointments'),
    path('changepass/<int:doc_id>/', views.changepass, name='changepass'),
    path('approve-leave/', views.approve_leave, name='approve_leave'),
    path('reject-leave/', views.reject_leave, name='reject_leave'), 
    path('doctors/appointments/<int:doc_id>/', views.doctors_appointments, name='doctors_appointments'),
    path('invoice/<int:donation_id>/', views.admins_invoiceview, name='admins_invoiceview'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('submit_medical_history/<int:patient_id>/', views.submit_medical_history, name='submit_medical_history'),
    path('doctors-prescription/<int:patient_id>/', views.doctors_prescription, name='doctors_prescription'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)