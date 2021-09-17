from CHP.models import *
from CHP.forms import *
from cloudinary.forms import cl_init_js_callbacks
from django.contrib.auth import *
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.http.request import QueryDict,MultiValueDict
from django.forms.models import model_to_dict

def home(request):
    return render(request,'home.html',{'categories':Categories.objects.all()})

def breifPage(request,category):
    allData = AllData.objects.filter(category=Categories.objects.get(name=category))
    return render(request,'breifPage.html',{'allData':allData})

def detailPage(request,category,id):
    data = AllData.objects.filter(id=id)[0]
    return render(request,'detailPage.html',{'data':data})

def dashboard(request):
    if request.user.is_authenticated:
        if set(['Verifier','Admin','Editor']).intersection(set(str(i) for i in request.user.groups.all()))!=set():
            return render(request,'admin/dashboard.html',{'user':request.user})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin')

def manage_users(request):
    if request.user.has_perm('CHP.view_user'):
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
        return render(request,'admin/manage_data.html',{'alldata':AllData.objects.all(),'categories':Categories.objects.all()})
    else:
        return HttpResponseRedirect('/signin')

def manage_data_cat(request,category):
    alldata = AllData.objects.filter(category=Categories.objects.get(name=category).id)
    return render(request,'admin/manage.html',{
            'name':f"{category} Data",'alldata':alldata,
            'category':Categories.objects.get(name=category)
        })

def add(request,name):
    if request.user.has_perm('CHP.add_'+name):
        if request.method == 'POST':
            if name == 'categories':
                form = AddCategoryForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added Category')
                    return HttpResponseRedirect('/manage-categories')
            elif name == 'user':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully added User')
                    return HttpResponseRedirect('/manage-users')
        else:
            if name == 'categories':
                sname="Category"
                form = AddCategoryForm()
            elif name == 'user':
                sname="User"
                form = SignUpForm()
            else:
                return HttpResponseRedirect('/dashboard')
            return render(request,'admin/add_edit.html',{'name':f'Add {sname}','form':form})
    else:
        return HttpResponseRedirect('/signin')


def add_data(request,category):
    if request.user.has_perm('CHP.add_alldata'):
        if request.method == 'POST':
            form = AddDataForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Successfully added Data')
                return HttpResponseRedirect(f'/manage/{category}')
        else:
            dataField = {}
            for k,v in model_to_dict(Categories.objects.get(name=category)).items():
                if k not in ['','id','icon'] and v!='':
                    dataField[k]=v
            form = AddDataForm()
            dataField['name'],dataField['phone1'],dataField['phone2'],dataField['phone3']="Name","Phone Number","2nd Phone Number","3rd Phone Number",
            dataField['email'],dataField['address1'],dataField['pincode'],dataField['city']="Email","Address","Pincode","City",
            dataField['state'],dataField['website'],dataField['mapUrl']="","Website","Map Location Link"
            return render(request,'admin/add_edit.html',{
                                        'name':f'Add Data','form':form,
                                        'dataField':dataField,'categoryId':Categories.objects.get(name=category).id,
                                        'categoryName':category
                                    }
                        )
    else:
        return HttpResponseRedirect('/signin')


def edit(request,name,id):
    if request.user.has_perm('CHP.change_'+name):
        if request.method == 'POST':
            if name == 'categories':
                data = Categories.objects.get(pk=id)
                form = AddCategoryForm(request.POST,request.FILES,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Successfully Changed Category')
                    return HttpResponseRedirect('/manage-categories')
            elif name == 'user':
                data = User.objects.get(pk=id)
                form = AdminUserChangeForm(request.POST,instance=data)
                if form.is_valid():
                    data.groups.clear()
                    data.groups.add(form.cleaned_data['usergroup'])
                    form.save()
                    messages.success(request,'Successfully Changed User')
                    return HttpResponseRedirect('/manage-users')
        else:
            if name == 'categories':
                sname="Category"
                data = Categories.objects.get(pk=id)
                form = AddCategoryForm(instance=data)
            elif name == 'user':
                sname="User"
                data = User.objects.get(pk=id)
                form = AdminUserChangeForm(instance=data)
            else:
                return HttpResponseRedirect('/dashboard')
            return render(request,'admin/add_edit.html',{'name':f'Edit {sname}','form':form,'everyDetail':data})
    else:
        return HttpResponseRedirect('/signin')


def edit_data(request,category,id):
    if request.user.has_perm('CHP.add_alldata'):
        if request.method == 'POST':
            data = AllData.objects.get(pk=id)
            form = AddDataForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,'Successfully Changed Data')
                return HttpResponseRedirect(f'/manage/{category}')
        else:
            dataField = {}
            for k,v in model_to_dict(Categories.objects.get(name=category)).items():
                if k not in ['','id','name','icon'] and v!='':
                    dataField[k]=v
            data = AllData.objects.get(pk=id)
            form = AddDataForm(instance=data)
            dataField['name'],dataField['phone1'],dataField['phone2'],dataField['phone3']="Name","Phone Number","2nd Phone Number","3rd Phone Number",
            dataField['email'],dataField['address'],dataField['landmark'],dataField['pincode'],dataField['city']="Email","Address","Landmark","Pincode","City",
            dataField['state'],dataField['website'],dataField['mapUrl']="","Website","Map Location Link"
            return render(request,'admin/add_edit.html',{
                                        'name':f'Edit Data','form':form,
                                        'dataField':dataField,'categoryId':Categories.objects.get(name=category).id,
                                        'categoryName':category,'id':id
                                    }
                        )
    else:
        return HttpResponseRedirect('/signin')

def delete(request,name,id):
    if request.user.has_perm('CHP.delete_'+name):
        if request.method == 'POST':
            if name == 'categories':
                category = Categories.objects.get(pk=id)
                category.delete()
                messages.success(request,'Successfully Deleted Category')
                return HttpResponseRedirect('/manage-categories')
            elif name == 'user':
                user = User.objects.get(pk=id)
                user.delete()
                messages.success(request,'Successfully Deleted User')
                return HttpResponseRedirect('/manage-users')
        else:
            if name == 'categories':
                messages.success(request,'Category Deletion Unsuccessful')
                return HttpResponseRedirect('/manage-categories')
            elif name == 'user':
                messages.success(request,'User Deletion Unsuccessful')
                return HttpResponseRedirect('/manage-users')
            else:
                return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/signin')

def delete_data(request,category,id):
    if request.user.has_perm('CHP.delete_alldata'):
        if request.method == 'POST':
            data = AllData.objects.get(pk=id)
            data.delete()
            messages.success(request,'Successfully Deleted Data')
            return HttpResponseRedirect(f'/manage/{category}')
        else:
            messages.success(request,'Data Deletion Unsuccessfull')
            return HttpResponseRedirect(f'/manage/{category}')
    else:
        return HttpResponseRedirect('/signin')