from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where email is the unique identifier instead of username.
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
