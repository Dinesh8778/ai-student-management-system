from django.db import models
from students.models import Student
from academics.models import Subject

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.student} - {self.subject}"