from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=250)
    email = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
