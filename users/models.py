from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    is_doc = models.BooleanField(default=False)
    designation = models.CharField(blank=True, null=True, max_length=100)
    hospital = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.email