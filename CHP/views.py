from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from CHP.token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
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
                current_site = get_current_site(request)
                mail_subject = 'Activate your ICHG account.'
                message = render_to_string('partials/email_template.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk))  ,
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                messages.success(request, 'Form submission successful Activation Link Was sent to email')
                return HttpResponseRedirect('/signin')
        else:
            form = SignUp()
        return render(request, 'signup.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def user_activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Account Activated')
        return HttpResponseRedirect('/signin')
    else:
        messages.success(request,'Activation link is invalid!')
        return HttpResponseRedirect('/signup')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'partials/changepass.html', {
        'form': form
    })

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

def manage_users(request):
    if request.user.is_authenticated:
        allusers = User.objects.all()
        return render(request,'partials/manage-users.html',{'users':allusers})
    else:
        return render('/signin')