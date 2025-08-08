from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,mobile,password=None):
        if not email:
            raise ValueError('User Must have Email ID')
        if not username:
            raise ValueError('Username is Mandatory')
        if not mobile:
            raise ValueError("mobile field Can't Blank")
        user=self.model(first_name=first_name,last_name=last_name,username=username,email=self.normalize_email(email),mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,username,email,mobile,password):
        user=self.create_user(first_name=first_name,last_name=last_name,username=username,email=email,mobile=mobile,password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    username=models.CharField(max_length=50,unique=True)
    mobile=models.CharField(max_length=10)
    join_date=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=20)

    #required
    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username','mobile']
    objects=MyAccountManager()
    def str(self):
        return self.email
    def has_perm(self,perm,object=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True
