from CHP.models import *
from CHP.forms import *
from django.contrib.auth import *
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse

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
                    return HttpResponseRedirect('/manage-categories')
            elif name == 'users':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added User')
                    return HttpResponseRedirect('/manage-users')
            elif name == 'alldata':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added User')
                    return HttpResponseRedirect('/manage-data')
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
            return render(request,'admin/add_edit.html',{'name':f'Add {sname}','form':form})
    else:
        return HttpResponseRedirect('/signin')

def edit(request,name,id):
    if request.user.has_perm('CHP.change_'+name):
        if request.method == 'POST':
            if name == 'categories':
                data = Categories.objects.get(pk=id)
                form = AddCategoryForm(request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully Changed Category')
                    return HttpResponseRedirect('/manage-categories')
            elif name == 'users':
                data = User.objects.get(pk=id)
                form = SignUpForm(request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully Changed User')
                    return HttpResponseRedirect('/manage-users')
            elif name == 'alldata':
                data = User.objects.get(pk=id)
                form = SignUpForm(request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully Changed Data')
                    return HttpResponseRedirect('/manage-data')
        else:
            if name == 'categories':
                sname="Category"
                data = Categories.objects.get(pk=id)
                form = AddCategoryForm(instance=data)
            elif name == 'users':
                sname="User"
                data = User.objects.get(pk=id)
                form = SignUpForm(instance=data)
            elif name == 'alldata':
                sname="Data"
                data=AllData.objects.get(pk=id)
                form = SignUpForm(instance=data)
            else:
                return HttpResponseRedirect('/dashboard')
            return render(request,'admin/add_edit.html',{'name':f'Edit {sname}','form':form})
    else:
        return HttpResponseRedirect('/signin')

def json_test(request):
    data=list(Categories.objects.values())
    return JsonResponse(data,safe=False)