from django import forms
from cloudinary.forms import *
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,UserChangeForm
from CHP.models import *

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'validate'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'validate'}))
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
        labels = {'email':'Email','first_name':'First Name','last_name':'Last Name'}
        widgets = {k:forms.TextInput(attrs={'placeholder':v,'class':'validate'}) for k,v in labels.items()}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'placeholder':'Email','class':'validate'}))
    password = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'validate'}))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'placeholder':'Old Password','class':'validate'}))
    new_password1 = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'placeholder':'New Password','class':'validate'}))
    new_password2 = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'validate'}))
            
class ChangeUserProfileForm(UserChangeForm):
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = {'first_name','last_name','password'}
        labels = {'first_name':'First Name','last_name':'Last Name'}
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'validate'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name','class':'validate'}),
        }

class AdminUserChangeForm(UserChangeForm):
    password = forms.PasswordInput(attrs={'type':'hidden'})
    usergroup =  forms.ModelChoiceField(Group.objects.all(),label="User Permission Level", empty_label=None)
    class Meta:
        model = User
        fields = {'is_superuser','is_active','is_staff','usergroup'}
        labels = {'is_superuser':'Set Admin','is_active':'Set Active','is_staff':'Make Staff Member'}
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = [
            'name', 'icon', 'field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7',
            'field8', 'field9', 'field10', 'field11', 'field12', 'field13', 'field14', 'field15',
            'field16', 'field17', 'field18', 'field19', 'field20', 'field21',
            'field22', 'field23', 'field24','is_shown'
        ]
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name','class':'validate'}),
            'field1':forms.TextInput(attrs={'placeholder':'Field 1 Name','class':'validate'}),
            'field2':forms.TextInput(attrs={'placeholder':'Field 2 Name','class':'validate'}),
            'field3':forms.TextInput(attrs={'placeholder':'Field 3 Name','class':'validate'}),
            'field4':forms.TextInput(attrs={'placeholder':'Field 4 Name','class':'validate'}),
            'field5':forms.TextInput(attrs={'placeholder':'Field 5 Name','class':'validate'}),
            'field6':forms.TextInput(attrs={'placeholder':'Field 6 Name','class':'validate'}),
            'field7':forms.TextInput(attrs={'placeholder':'Field 7 Name','class':'validate'}),
            'field8':forms.TextInput(attrs={'placeholder':'Field 8 Name','class':'validate'}),
            'field9':forms.TextInput(attrs={'placeholder':'Field 9 Name','class':'validate'}),
            'field10':forms.TextInput(attrs={'placeholder':'Field 10 Name','class':'validate'}),
            'field11':forms.TextInput(attrs={'placeholder':'Field 11 Name','class':'validate'}),
            'field12':forms.TextInput(attrs={'placeholder':'Field 12 Name','class':'validate'}),
            'field13':forms.TextInput(attrs={'placeholder':'Field 12 Name','class':'validate'}),
            'field14':forms.TextInput(attrs={'placeholder':'Field 14 Name','class':'validate'}),
            'field15':forms.TextInput(attrs={'placeholder':'Field 16 Name','class':'validate'}),
            'field16':forms.TextInput(attrs={'placeholder':'Field 16 Name','class':'validate'}),
            'field17':forms.TextInput(attrs={'placeholder':'Field 17 Name','class':'validate'}),
            'field18':forms.TextInput(attrs={'placeholder':'Field 18 Name','class':'validate'}),
            'field19':forms.TextInput(attrs={'placeholder':'Field 19 Name','class':'validate'}),
            'field20':forms.TextInput(attrs={'placeholder':'Field 20 Name','class':'validate'}),
            'field21':forms.TextInput(attrs={'placeholder':'Field 21 Name','class':'validate'}),
            'field22':forms.TextInput(attrs={'placeholder':'Field 22 Name','class':'validate'}),
            'field23':forms.TextInput(attrs={'placeholder':'Field 23 Name','class':'validate'}),
            'field24':forms.TextInput(attrs={'placeholder':'Field 24 Name','class':'validate'}),
            'is_shown':forms.Select(choices=((True,'Visible'),(False,'Hidden'))),
        }


class AddDataForm(forms.ModelForm):
    category =  forms.ModelChoiceField(Categories.objects.all(), empty_label=None)
    class Meta:
        model = AllData
        fields = [
            'category','field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7','field8',
            'field9', 'field10', 'field11', 'field12', 'field13', 'field14', 'field15','field16','field17',
            'field18', 'field19', 'field20', 'field21','field22', 'field23', 'field24','is_shown','is_verified'
        ]
        widgets={
            'is_verified':forms.Select(choices=((True,'Verified'),(False,'Unverified'))),
            'is_shown':forms.Select(choices=((True,'Visible'),(False,'Hidden'))),
        }