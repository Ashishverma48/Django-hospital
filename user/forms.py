from django import forms

from .models import *

class PatientForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for patient in self.fields.values():
            patient.widget.attrs['placeholder'] = f'Enter {patient.label} *'



class DoctorForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Doctor
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for doctor in self.fields.values():
            doctor.widget.attrs['placeholder']=f'Enter {doctor.label} *'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields='__all__'
