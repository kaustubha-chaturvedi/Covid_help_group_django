from django.db import models

class Categories(models.Model):
    name=models.TextField()
    icon=models.TextField()