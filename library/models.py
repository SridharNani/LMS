from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

class MyUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) #unique email feild
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS

    def __str__(self):
        return str(self.username)
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
 
    def __str__(self):
        return str(self.name)

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)



