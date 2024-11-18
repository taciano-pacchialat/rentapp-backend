from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, dni, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not dni:
            raise ValueError('Users must have a DNI number')

        user = self.model(
            email=self.normalize_email(email),
            dni=dni,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, dni, password=None):
        user = self.create_user(
            email,
            password=password,
            dni=dni,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    dni = models.IntegerField(max_length=8, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dni']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
