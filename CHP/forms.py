from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
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
            
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = [
            'name', 'icon', 'field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7',
            'field8', 'field9', 'field10', 'field11', 'field12', 'field13', 'field14', 'field15',
            'field16', 'field17', 'field18', 'field19', 'field20', 'field21',
            'field22', 'field23', 'field24'
        ]
        labels = {
            'name':'Name','icon':'Icon','field1':'Field 1 Name','field2':'Field 2 Name',
            'field3':'Field 3 Name','field4':'Field 4 Name','field5':'Field 5 Name','field6':'Field 6 Name',
            'field7':'Field 7 Name','field8':'Field 8 Name','field9':'Field 9 Name','field10':'Field 10 Name',
            'field11':'Field 11 Name','field12':'Field 12 Name','field13':'Field 13 Name','field14':'Field 14 Name',
            'field15':'Field 15 Name','field16':'Field 16 Name','field17':'Field 17 Name','field18':'Field 18 Name',
            'field19':'Field 19 Name','field20':'Field 20 Name','field21':'Field 21 Name','field22':'Field 22 Name',
            'field23':'Field 23 Name','field24':'Field 24 Name',
        }
        widgets = {k:forms.TextInput(attrs={'placeholder':v,'class':'validate'}) for k,v in labels.items()}