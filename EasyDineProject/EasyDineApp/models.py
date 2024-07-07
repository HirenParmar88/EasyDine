from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

#book table model
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    people = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
'''class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username'''

class login(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username must be set')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = login()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    










    

