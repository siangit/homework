from django.db import models
from common.models import CommonModel
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser, CommonModel):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.username