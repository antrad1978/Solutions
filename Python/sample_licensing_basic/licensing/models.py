from django.db import models

from django.db import models
from django.utils import timezone


class License(models.Model):
    user = models.ForeignKey('auth.User')
    machine_id = models.CharField(max_length=64,unique=True)
    customer = models.CharField(max_length=256)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.customer
