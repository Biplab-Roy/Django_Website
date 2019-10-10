from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def gallery(request):
    return HttpResponse("<h1>Update coming soon</h1>")
def services(request):
    return HttpResponse("<h1>Update coming soon</h1>")
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')