from django.db import models

# Create your models here.
class Account(models.Model):
    accountName = models.CharField(max_length=100, blank=True, default='')
    userName = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='accounts', default='')


