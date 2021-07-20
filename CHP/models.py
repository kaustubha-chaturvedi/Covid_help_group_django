from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=255,blank=False)
    first_name = models.CharField(_('first name'),max_length=150,blank=True)
    last_name = models.CharField(_('last name'),max_length=150,blank=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_active = models.BooleanField(_('active'),default=True)
    date_joined = models.DateTimeField(_('date joined'),default=timezone.now)
  
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name+" "+self.last_name

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
    verified = models.BooleanField(_("Verified"),default=False)
    
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class AllData(models.Model):
    category = models.ForeignKey(Categories,related_name="category",on_delete=models.DO_NOTHING)
    data = models.JSONField()