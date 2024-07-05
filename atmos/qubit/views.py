from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse

def login(req):
    if req.POST: 
        phone=req.POST.get('phone','')
        print(phone)
    return render(req,'login.html')

# telegram_auth/views.py


def home(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        print(phone)
        # Handle form submission and logic here
        return HttpResponse("Form submitted with phone number: " + phone)
    return render(request, 'home.html')

def auth(req):
    if req.method=='POST':
        u=req.POST.get('input1')
        p=req.POST.get('input2')
        n=req.POST.get('input3')
        i=req.POST.get('input4')
        print(i,n,p,u)

    return render(req,'auth.html')





