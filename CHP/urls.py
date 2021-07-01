from django.urls import path,include
from CHP.views import *
urlpatterns=[
    path('',home),
    path('icons',searchIcon)
]