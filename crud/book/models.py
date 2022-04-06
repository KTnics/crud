from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return str(self.author)


