from contextlib import nullcontext

from django.db import models

# Create your models here.

class Task(models.Model):
    # id = models.IntegerField(primary_key=true)
    title = models.CharField(default=nullcontext, max_length=20)
    description = models.CharField(default=nullcontext, max_length=300)
