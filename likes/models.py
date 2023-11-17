from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectId = models.PositiveIntegerField()
    contentObject = GenericForeignKey()
