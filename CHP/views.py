from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html')

def searchIcon(request):
    return render(request,'tabler-icons.html')