from django.db import models


class Room(models.Model):

    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=50)

    floor = models.IntegerField()

    total_beds = models.IntegerField()
    available_beds = models.IntegerField()

    rent = models.IntegerField()

    room_image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return self.room_number