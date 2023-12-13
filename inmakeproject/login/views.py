from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
           if User.objects.filter(username=username).exists():
              # print("email exists")
              messages.info(request, "User exists")
              return redirect('register')
           elif User.objects.filter(email=email).exists():
                print("email exists")
                messages.info(request, "Email id exist")
                return redirect('register')
           else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "Password not mached")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
