from django.shortcuts import render,HttpResponse
from CHP.models import *

def home(request):
    return render(request,'home.html',{'categories':Categories.objects.all()})

def searchIcon(request):
    return render(request,'tabler-icons.html')