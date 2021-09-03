from ICHG.settings import STATE_LIST
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin,Group
from django.utils.translation import ugettext_lazy as _
from cloudinary.models import CloudinaryField


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
        extra_fields.setdefault('is_active', True)

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
    is_active = models.BooleanField(_('active'),default=False)
    is_superuser = models.BooleanField(_('superuser'),default=False)
    date_joined = models.DateTimeField(_('date joined'),default=timezone.now)
    usergroup = models.ForeignKey(Group,related_name="groups",on_delete=models.SET_NULL,null=True)
  
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name+" "+self.last_name

class Categories(models.Model):
    name = models.TextField()
    icon = CloudinaryField(overwrite=True,)
    # input fields for category
    field1 = models.TextField(null=True,blank=True)
    field2 = models.TextField(null=True,blank=True)
    field3 = models.TextField(null=True,blank=True)
    field4 = models.TextField(null=True,blank=True)
    field5 = models.TextField(null=True,blank=True)
    field6 = models.TextField(null=True,blank=True)
    field7 = models.TextField(null=True,blank=True)
    field8 = models.TextField(null=True,blank=True)
    field9 = models.TextField(null=True,blank=True)
    field10 = models.TextField(null=True,blank=True)
    field11 = models.TextField(null=True,blank=True)
    field12 = models.TextField(null=True,blank=True)
    field13 = models.TextField(null=True,blank=True)
    field14 = models.TextField(null=True,blank=True)
    field15 = models.TextField(null=True,blank=True)
    field16 = models.TextField(null=True,blank=True)
    field17 = models.TextField(null=True,blank=True)
    field18 = models.TextField(null=True,blank=True)
    field19 = models.TextField(null=True,blank=True)
    field20 = models.TextField(null=True,blank=True)
    is_shown = models.BooleanField(default=True)
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class AllData(models.Model):
    category = models.ForeignKey(Categories,related_name="category",on_delete=models.SET_NULL,null=True)
    name = models.TextField(null=True,blank=True)
    phone1 = models.TextField(null=True,blank=True)
    phone2 = models.TextField(null=True,blank=True)
    phone3 = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    landmark = models.TextField(null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    city = models.TextField(null=True,blank=True)
    state = models.CharField(
        max_length=30,
        choices=STATE_LIST,
        default='DL'
    )
    mapUrl = models.URLField(null=True,blank=True)
    field1 = models.TextField(null=True,blank=True)
    field2 = models.TextField(null=True,blank=True)
    field3 = models.TextField(null=True,blank=True)
    field4 = models.TextField(null=True,blank=True)
    field5 = models.TextField(null=True,blank=True)
    field6 = models.TextField(null=True,blank=True)
    field7 = models.TextField(null=True,blank=True)
    field8 = models.TextField(null=True,blank=True)
    field9 = models.TextField(null=True,blank=True)
    field10 = models.TextField(null=True,blank=True)
    field11 = models.TextField(null=True,blank=True)
    field12 = models.TextField(null=True,blank=True)
    field13 = models.TextField(null=True,blank=True)
    field14 = models.TextField(null=True,blank=True)
    field15 = models.TextField(null=True,blank=True)
    field16 = models.TextField(null=True,blank=True)
    field17 = models.TextField(null=True,blank=True)
    field18 = models.TextField(null=True,blank=True)
    field19 = models.TextField(null=True,blank=True)
    field20 = models.TextField(null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    is_shown = models.BooleanField(default=False)