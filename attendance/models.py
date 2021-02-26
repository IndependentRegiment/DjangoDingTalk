from django.db import models

# Create your models here.
class onjobUserInfo(models.Model):
    userid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
