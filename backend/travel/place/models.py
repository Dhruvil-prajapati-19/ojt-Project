from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class card(models.Model):
    city = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    Description =  models.CharField(max_length=250)
    images = models.ImageField(upload_to='avatars/', blank=True, null=True)



