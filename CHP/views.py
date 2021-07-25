from CHP.models import *
from CHP.forms import *
from django.contrib.auth import *
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
            return render(request,'admin/dashboard.html',{'user':request.user})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin')

def manage_users(request):
    if request.user.has_perm('CHP.view_users'):
        allusers = User.objects.all()
        return render(request,'admin/manage.html',{'name':'Users','users':allusers})
    else:
        return HttpResponseRedirect('/signin')

def manage_categories(request):
    if request.user.has_perm('CHP.view_categories'):
        categories = Categories.objects.all()
        return render(request,'admin/manage.html',{'name':'Categories','categories':categories})
    else:
        return HttpResponseRedirect('/signin')

def manage_data(request):
    if request.user.has_perm('CHP.view_alldata'):
        allData = AllData.objects.all()
        return render(request,'admin/manage.html',{'name':'Data','alldata':allData})
    else:
        return HttpResponseRedirect('/signin')

def add(request,name):
    if request.user.has_perm('CHP.add_'+name):
        if request.method == 'POST':
            if name == 'categories':
                form = AddCategoryForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added Category')
                    return HttpResponseRedirect('manage-categories')
            elif name == 'users':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added User')
                    return HttpResponseRedirect('manage-users')
            elif name == 'alldata':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added User')
                    return HttpResponseRedirect('manage-users')
        else:
            if name == 'categories':
                sname="Category"
                form = AddCategoryForm()
            elif name == 'users':
                sname="User"
                form = SignUpForm()
            elif name == 'alldata':
                sname="Data"
                form = SignUpForm()
            else:
                return HttpResponseRedirect('/dashboard')
            return render(request,'admin/add.html',{'name':sname,'form':form})
    else:
        return HttpResponseRedirect('/signin')