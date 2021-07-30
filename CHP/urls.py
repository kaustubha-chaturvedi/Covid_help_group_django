from django.urls import path,include
from django.contrib.auth import views as auth_views
from CHP.views import *
from CHP.authFunctions import *

authFunctionsList = [
    path('signup',user_signup),
    path('signin',user_login,name='signin'),
    path('signout',user_logout),
    path('changepass',change_password, name='change_password'),
    path('changeprof',change_profile, name='change_profile'),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}',user_activation, name='activate'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='partials/password_reset/form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='partials/password_reset/done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='partials/password_reset/confirm.html'),name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='partials/password_reset/complete.html'),name='password_reset_complete')
]

adminFunctionsList=[
    path('dashboard',dashboard),
    path('manage-categories',manage_categories,name='manage-categories'),
    path('manage-data',manage_data,name='manage-data'),
    path('manage-users',manage_users,name='manage-users'),
    path('manage/<str:category>',manage_data_cat,),
    path('add/<str:name>',add,name='add'),
    path('addData/<str:category>',add_data,name='addData'),
    path('edit/<str:name>/<int:id>',edit,name='edit'),
    path('editData/<str:category>/<int:id>',edit_data,name='editData'),
    path('delete/<str:name>/<int:id>',delete,name='delete'),
    path('deleteData/<str:category>/<int:id>',delete_data,name='deleteData'),
]

genericUrls = [
    path('',home),
    path('breifpage/<str:category>',breifPage),
]
urlpatterns=[path('icons',searchIcon)]+authFunctionsList+genericUrls+adminFunctionsList