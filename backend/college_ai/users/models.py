from django.db import models
from academics.models import Subject

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name