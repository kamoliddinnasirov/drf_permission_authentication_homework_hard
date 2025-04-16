from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')



class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teaching_courses')
    students = models.ManyToManyField(User, related_name='enrolled_courses')