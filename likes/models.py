from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectId = models.PositiveIntegerField()
    contentObject = GenericForeignKey()
