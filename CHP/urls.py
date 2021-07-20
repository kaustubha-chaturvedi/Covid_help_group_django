from django.urls import path,include
from CHP.views import *
urlpatterns=[
    path('',home),
    path('icons',searchIcon),
    path('signup',user_signup),
    path('signin',user_login),
    path('signout',user_logout),
    path('dashboard',dashboard),
    path('breifpage/<str:category>',breifPage)
]