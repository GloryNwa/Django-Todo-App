from __future__ import unicode_literals
from datetime import datetime
from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title
