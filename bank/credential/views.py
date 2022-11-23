from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from bankapp.models import Bank


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('about')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def about(request):
    return render(request,'about.html')
def sub(request):
    return render(request,'sub.html')
def index(request):
    return render(request,'index.html')

def new(request):
    # if request.method=='POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     address = request.POST.get('address')
    #     bank=Bank(name=name,email=email,address=address)
    #     bank.save()
    #     messages.info(request, 'application accepted')
    # #     return redirect('new')
    # #
    # # if 'logout' in request.POST:
    # #     auth.logout(request)
    # #     return redirect('/')
    return render(request, 'new.html')