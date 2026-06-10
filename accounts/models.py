from django.db import models

class Warden(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    photo = models.ImageField(upload_to='warden/')

    def __str__(self):
        return self.name