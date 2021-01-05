from django.db import models
from django.utils import timezone

class Signup(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 120, null = True, blank = False)
    nickname = models.CharField(max_length = 120, null = True, blank = False)
    email = models.CharField(max_length = 120, null = True, blank = False)


# Create your models here.
