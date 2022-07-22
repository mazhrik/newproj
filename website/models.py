from django.db import models


# Create your models here.
class tablee(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()

