from django.contrib.auth.models import AbstractUser
from django.db import models


#class User(AbstractUser):
#    pass


class Mem(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT, related_name='mems')
    url = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
