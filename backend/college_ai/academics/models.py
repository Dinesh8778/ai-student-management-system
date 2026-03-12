from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Class(models.Model):

    DEPARTMENT_CHOICES = [
        ('IT', 'Information Technology'),
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
    ]

    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]

    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.department} - Year {self.year}"