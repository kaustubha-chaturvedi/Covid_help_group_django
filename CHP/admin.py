from django.contrib import admin
from CHP.models import *

@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=['id','name','icon']