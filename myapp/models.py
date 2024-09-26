from uuid import uuid4
from django.db import models
from datetime import datetime


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100,null=False, unique=True)
    description = models.TextField(null=False, max_length=200)
    date_created = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
