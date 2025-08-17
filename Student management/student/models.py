from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_roll = models.IntegerField()
    student_email = models.EmailField()
    student_contact =models.BigIntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student_name
