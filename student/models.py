from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    grade = models.IntegerField()  # Ensure grade is an IntegerField
    email = models.EmailField()
    date_of_birth = models.DateField()