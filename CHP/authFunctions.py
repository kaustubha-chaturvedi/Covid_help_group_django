from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import Group
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from six import text_type
from CHP.forms import *


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name="Subscriber") 
                user.groups.add(group)
                current_site = get_current_site(request)
                mail_subject = 'Activate your ICHG account.'
                message = render_to_string('auth/email_template.html', {
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
            form = SignUpForm()
        return render(request, 'auth/signup.html', {'form':form})
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

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=email,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    return HttpResponseRedirect('/')    
        else:
            form = LoginForm()
            return render(request, 'auth/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/changepass')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'auth/changepass.html', {'form': form})

def change_profile(request):
    if request.method == 'POST':
        form = ChangeUserProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your Profile was successfully updated!')
            return HttpResponseRedirect('/changeprof')
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponseRedirect('/changeprof')
    else:
        form = ChangeUserProfileForm(instance=request.user)
    return render(request, 'auth/changeprof.html', {'form': form,'email':request.user.email})