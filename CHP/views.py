from CHP.models import *
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages

def searchIcon(request):
    return render(request,'tabler-icons.html')

def home(request):
    return render(request,'home.html',{'categories':Categories.objects.all()})

def breifPage(request,category):
    return render(request,'breifPage.html',{'category':category})


def dashboard(request):
    if request.user.is_authenticated:
        if set(['Verifier','Admin','Editor']).intersection(set(str(i) for i in request.user.groups.all()))!=set():
            return render(request,'dashboard.html',{'user':request.user})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin')

def manage_users(request):
    if request.user.is_authenticated:
        allusers = User.objects.all()
        return render(request,'partials/manage-users.html',{'users':allusers})
    else:
        return render('/signin')