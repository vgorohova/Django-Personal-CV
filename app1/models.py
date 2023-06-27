from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    cod = models.IntegerField(default=0)
    data_inscr = models.DateField()