import datetime

from django.db import models
from django.utils import timezone

class Counter(models.Model):
    label = models.CharField(max_length=48)
    created_date = models.DateTimeField('date created')
    value = models.IntegerField(default=0)
    
    def __str__(self):
        return self.label