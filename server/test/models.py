from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField


class BilibiliUsers(models.Model):

    uid = models.BigIntegerField(primary_key=True)
    follower = models.BigIntegerField()
    following = models.BigIntegerField()
    archive = models.BigIntegerField()
    likes = models.BigIntegerField()
    vedios = JSONField()

    class Meta:
        db_table = "bilibili_users"
