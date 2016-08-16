from __future__ import unicode_literals

from django.db import models
from django.utils import timezone



# Create your models here.
class UrlList(models.Model):
    title = models.CharField(max_length = 200)
    created_date = models.DateTimeField(
            default=timezone.now)
    posting_url = models.URLField(max_length = 200, default = '')
    posting_priority = models.BooleanField(default = False)
    text = models.TextField(default=" ")


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
