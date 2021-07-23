from django.urls import path,include
from CHP.views import *
urlpatterns=[
    path('',home),
    path('icons',searchIcon),
    path('signup',user_signup),
    path('signin',user_login),
    path('signout',user_logout),
    path('dashboard',dashboard),
    path('manage-users',manage_users),
    path('breifpage/<str:category>',breifPage),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}',user_activation, name='activate'),
    path('changepass',change_password, name='change_password'),
]