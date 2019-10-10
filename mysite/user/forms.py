from .models import Patient_Profile
from django import forms

class Registrationform(forms.ModelForm):
    Confirm_passsword = forms.CharField()
    class Meta:
        model = Patient_Profile
        fields = ['Patient_name','Patient_avatar','Patient_mail','Patient_age','Patient_gender','Patient_password','Patient_password']
        labels = {
            'Patient_name':'Name',
            'Patient_avatar':'Upload profile picture',
            'Patient_mail':'Email',
            'Patient_age':'Age',
            'Patient_gender':'Gender',
            'Patient_password':'Enter Password',
            'Patient_password':'Confirm Password'
        }

class Loginform(forms.ModelForm):
    class Meta:
        model = Patient_Profile
        fields = ['Patient_mail','Patient_password']
        labels = {
            'Patient_mail':'Email',
            'Patient_password':'Enter Password'
        }

