from django.db import models
from django.contrib.auth.models import AbstractUser


    
class User(AbstractUser):

    is_active_account = models.BooleanField(default=True)
    role = models.CharField(max_length=10, choices=(('admin', 'admin'), ('manager', 'manager'),('member','member')), default='member')
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username',]


