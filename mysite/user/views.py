from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Registrationform, Loginform
from .models import Patient_Profile
from django.contrib import messages

# Create your views here.

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup(request):
    if request.method == "POST":
        form = Registrationform(request.POST)
        password1 = form['Patient_password'].value()
        password2 = form['Confirm_passsword'].value()
        if password1==password2:
            if Patient_Profile.objects.filter(Patient_mail = form['Patient_mail'].value()).exists():
                messages.info(request,'Username Taken')
                return render(request,'signup_user.html',{"form":form})
            else:
                if form.is_valid():
                    form.save()
                    return redirect('Profile_url')
                else:
                    form = Registrationform()
                    return render(request,'signup_user.html',{"form":form})
        else:
            messages.info(request,'Password did not match')
            return render(request,'signup_user.html',{"form":form})
    else:
        form = Registrationform()
        return render(request,'signup_user.html',{"form":form})

def signin(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        username = form['Patient_mail'].value()
        password = form['Patient_password'].value()
        Patients = Patient_Profile.objects.all()
        for patient in Patients:
            if patient.Patient_mail == username and patient.Patient_password == password:
                return redirect('Profile_url')
        messages.info(request,'Username or Password is incorrect')
        return render(request,'login_user.html',{"form":form})
    else:
        form = Loginform()
        return render(request,'login_user.html',{"form":form})

@csrf_protect
def profile(request):
    return render(request,'dashbord_user.html')