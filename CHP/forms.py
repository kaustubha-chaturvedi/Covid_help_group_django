from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm,UsernameField
from CHP.models import User

class CustomUserCreationFormForAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

class CustomUserChangeFormForAdmin(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class SignUp(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'validate'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'validate'}))
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
        labels = {'email':'Email','first_name':'First Name','last_name':'Last Name'}
        widgets = {
                'email':forms.EmailInput(attrs={'placeholder':'Email','class':'validate'}),
                'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'validate'}),
                'last_name':forms.TextInput(attrs={'placeholder':'Last Name','class':'validate'})
            }

class Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'placeholder':'Email','class':'validate'}))
    password = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'validate'}))