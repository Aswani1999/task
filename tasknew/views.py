from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasknew.forms import bankform
from tasknew.models import formmodel


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


# Create your views here.
def register(request):
    # name="india"
    # return render(request,"home.html",{'obj':name})
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')

        else:
            print("password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    return render(request,"newpage.html")
def appform(request):
    return render(request, "appform.html")
def submit(request):
    return render(request,"submit.html")








