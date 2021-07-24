from django.urls import path,include
from django.contrib.auth import views as auth_views
from CHP.views import *
from CHP.authFunctions import *
urlpatterns=[
    path('',home),
    path('icons',searchIcon),
    path('signup',user_signup),
    path('signin',user_login,name='signin'),
    path('signout',user_logout),
    path('dashboard',dashboard),
    path('manage-users',manage_users),
    path('breifpage/<str:category>',breifPage),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}',user_activation, name='activate'),
    path('changepass',change_password, name='change_password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='partials/password_reset/form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='partials/password_reset/done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='partials/password_reset/confirm.html'),name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='partials/password_reset/complete.html'),name='password_reset_complete')
]