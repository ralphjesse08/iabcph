from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_cryptography.fields import encrypt

# Create your models here.
# Base User Database
class UserManager(BaseUserManager):
    def create_user(self, email,firstName, middleName, lastName, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('Users must have an Email')      
        if not firstName:
            raise ValueError('Users must have a First Name')
        if not middleName:
            raise ValueError('Users must have a Middle Name')    
        if not lastName:
            raise ValueError('Users must have a Last Name')        

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            middleName=middleName,
            lastName=lastName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,firstName, middleName, lastName, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(
            email,
            password=password,
            firstName=firstName,
            middleName=middleName,
            lastName=lastName
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstName = encrypt(models.CharField(max_length=100))
    middleName = encrypt(models.CharField(max_length=100))
    lastName = encrypt(models.CharField(max_length=100))

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_nonmember = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_judge = models.BooleanField(default=False)
    is_bidder = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_inactive = models.DateTimeField(verbose_name='date inactive', null=True, blank=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'middleName', 'lastName',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
        
