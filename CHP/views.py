from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from CHP.models import *
from CHP.forms import *

def searchIcon(request):
    return render(request,'tabler-icons.html')

def home(request):
    return render(request,'home.html',{'categories':Categories.objects.all()})

def breifPage(request,category):
    return render(request,'breifPage.html',{'category':category})

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUp(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name="Subscriber") 
                user.groups.add(group)
        else:
            form = SignUp()
        return render(request, 'signup.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Login(request=request,data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=email,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard')
        else:
            form = Login()
            return render(request, 'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'user':request.user})
    else:
        return HttpResponseRedirect('/signin')