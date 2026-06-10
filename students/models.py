from django.db import models
from rooms.models import Room
class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    photo = models.ImageField(upload_to='students/')
    id_proof = models.FileField(upload_to='idproof/')

    joining_date = models.DateField(auto_now_add=True)

    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name