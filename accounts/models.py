from django.db import models
from django.utils import timezone

#import User Model
from django.contrib.auth.models import User

class Signup(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    #Foregin key connection failed (should be fixed)
    name = models.CharField(max_length = 120, null = True, blank = False)
    nickname = models.CharField(max_length = 120, null = True, blank = False)
    email = models.CharField(max_length = 120, null = True, blank = False)
 
    def __str__(self):
        return self.email

