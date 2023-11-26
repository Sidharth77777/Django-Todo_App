from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, user_class, user_division, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, full_name=full_name, user_class=user_class, user_division=user_division, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, user_class, user_division, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, user_class, user_division, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    CLASS_CHOICES = (
        ('1', '10'),
        # Add more choices if needed
    )
    
    DIVISION_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        # Add more choices if needed
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    user_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    user_division = models.CharField(max_length=1, choices=DIVISION_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'user_class', 'user_division']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
