from django.db import models
from academics.models import Class

class Student(models.Model):

    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=12, unique=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.regno} - {self.name}"