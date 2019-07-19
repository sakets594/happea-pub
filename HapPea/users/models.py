from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import *

# from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='profile', on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    contactnu=models.CharField(max_length=10,null=True,blank=True)
    #contactnu=PhoneNumberField("contactnu",null=True, blank=True)
    agegroup=models.IntegerField("agegroup",choices=AGEGROUP_CHOICES, default=0) 
    gender=models.IntegerField("gender",choices=GENDER_CHOICES, default=0) 



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)