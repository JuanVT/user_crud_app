from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.DecimalField(decimal_places=0, max_digits=30, blank=True, null=True)

    bio = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=30, blank=True, null=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
