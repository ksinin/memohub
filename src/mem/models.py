from django.db import models


class Mem(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT, related_name='mems')
    url = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("auth.User", related_name='mem_like')


class UserFollowing(models.Model):
    user = models.ForeignKey("auth.User", related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey("auth.User", related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
