from django.db import models

class Categories(models.Model):
    name = models.TextField()
    icon = models.TextField()
    # input fields for category
    field1 = models.TextField(null=True)
    field2 = models.TextField(null=True)
    field3 = models.TextField(null=True)
    field4 = models.TextField(null=True)
    field5 = models.TextField(null=True)
    field6 = models.TextField(null=True)
    field7 = models.TextField(null=True)
    field8 = models.TextField(null=True)
    field9 = models.TextField(null=True)
    field10 = models.TextField(null=True)
    field11 = models.TextField(null=True)
    field12 = models.TextField(null=True)
    field13 = models.TextField(null=True)
    field14 = models.TextField(null=True)
    field15 = models.TextField(null=True)
    field16 = models.TextField(null=True)
    field17 = models.TextField(null=True)
    field18 = models.TextField(null=True)
    field19 = models.TextField(null=True)
    field20 = models.TextField(null=True)
    field21 = models.TextField(null=True)
    field22 = models.TextField(null=True)
    field23 = models.TextField(null=True)
    field24 = models.TextField(null=True)
    field25 = models.TextField(null=True)
    
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class AllData(models.Model):
    category = models.ForeignKey(Categories,related_name="category",on_delete=models.DO_NOTHING)
    data = models.JSONField()