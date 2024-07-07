from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    post = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    about = models.TextField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name