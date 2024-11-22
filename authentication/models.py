from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, name, email, dni, password=None):
        if not name:
            raise ValueError('Users must have a name')
        if not email:
            raise ValueError('Users must have an email address')
        if not dni:
            raise ValueError('Users must have a DNI number')
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            dni=dni,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, dni, password=None):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
            dni=dni,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z][a-zA-Z ]*(?: [A-Z][a-zA-Z ]*)* [A-Z][a-zA-Z ]*(?: [A-Z][a-zA-Z ]*)*$',
                message='Name must be alphabetic',
                code='invalid_name'
            )
        ]
    )
    email = models.EmailField(unique=True)
    dni = models.IntegerField(validators=[
        RegexValidator(
            regex=r'^\d{7,8}$',
            message='DNI must be 7 or 8 digits',
            code='invalid_dni'
        )
    ], unique=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
            )
        ]
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)  

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dni', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
