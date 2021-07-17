from django.contrib import admin
from CHP.models import *

#Admin Settings
admin.site.site_header="ICHG Admin"
#Admin Settings
@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=['name','id']