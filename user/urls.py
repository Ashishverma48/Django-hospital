from django.urls import path
from .views import *
urlpatterns = [
    path("",viewHome, name="home"),
    path('patient/',viewPatient,name='patient'),
    path('doctor/',viewDoctor,name='doctor'),
    path('allpatient/',viewAllPatientDetails,name='allpatient'),
    path('alldoctor/',viewAllDoctorDetails,name='alldoctor'),
    path('createblog/',createBlogPost,name='createblog'),
    path('patientp/',patientPost,name=''),
    path('doctorp/',doctorPost,name='doctorPost'),
    path('viewblog/',viewBlogPost,name='viewblog'),


    

]
