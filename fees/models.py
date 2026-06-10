from django.db import models
from students.models import Student


class Fee(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    month = models.CharField(max_length=20)
    amount = models.IntegerField()

    status = models.CharField(max_length=20, default="Pending")

    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.student.name