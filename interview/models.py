from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Interview(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200 ,null=True)
    comment = models.TextField()
    start_date = models.DateTimeField(
            default=timezone.now)
    end_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
