from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def viewHome(request):
    return render(request,'user/home.html')



def viewPatient(request):
   if request.method =='GET':
       
       frm_unbound = PatientForm()
       data = {
            'forms':frm_unbound
        }
       return render(request,'user/patient.html',context=data)
   elif request.method =='POST':
       frm_bound = PatientForm(request.POST,files=request.FILES)
       password1 = request.POST.get('Password','NA')
       password2 = request.POST.get('ConfirmPassword','NA')
       data = {
           'forms':frm_bound
       }
       if frm_bound.is_valid:
           if password1==password2:
               frm_bound.save()
        
               return HttpResponse('<h1>Patient Ragistration Successfull </h1>')
           else:
                data['error']='Password Not Match !'
                    
                return render(request,'user/patient.html',context=data)
           
       else:
            return render(request,'user/patient.html',context=data)
       

def viewDoctor(request):
    if request.method == 'GET':
        frm_unbound = DoctorForm()
        data = {
            'forms':frm_unbound
        }
        return render(request,'user/doctor.html',context=data)
    elif request.method =='POST':
        frm_bound = DoctorForm(request.POST,files = request.FILES)
        password1 = request.POST.get('Password','NA')
        password2 = request.POST.get('ConfirmPassword','NA')
        data = {
           'forms':frm_bound
        }
        if frm_bound.is_valid():
            if password1==password2:
                frm_bound.save()
                return HttpResponse('<h1>Docter Ragitration </h1>')

            else:
                data['error']='Password Not Match !'
                return  render(request,'user/doctor.html',data)
        else:
            return render(request,'user/doctor.html',data)


def viewAllPatientDetails(request):
    if request.method == 'GET':
        allpatient = Patient.objects.all()
        data = {
            "allpatient":allpatient
        }
      

        return render(request,'user/showPatientDetails.html',data)
    

def viewAllDoctorDetails(request):
    if request.method == 'GET':
        alldoctor = Doctor.objects.all()
        data = {
            "alldoctor":alldoctor
        }
      

        return render(request,'user/showDoctorDetails.html',data)

               

