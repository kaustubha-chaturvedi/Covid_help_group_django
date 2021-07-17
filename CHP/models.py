from django.db import models

class Categories(models.Model):
    name=models.TextField()
    icon=models.TextField()
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name