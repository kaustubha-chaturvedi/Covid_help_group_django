from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from CHP.models import *
from CHP.forms import *

#Admin Settings
admin.site.site_header="ICHG Admin"
#Admin Settings

class CustomUserAdmin(UserAdmin):
    add_form = SignUp
    form = CustomUserChangeFormForAdmin
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)

@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=['name','id']

@admin.register(AllData)
class AllDataAdmin(admin.ModelAdmin):
    list_display=['category','data']