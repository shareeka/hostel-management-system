from django.db import models
from students.models import Student


class Complaint(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(max_length=20, default="Pending")

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title