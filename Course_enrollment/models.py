from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class StatusChoice(models.TextChoices):
        INSTRUCTOR='Instructor'
        STUDENT='Student'
    
    email = models.EmailField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    role = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.STUDENT,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    class StatusChoice(models.TextChoices):
        ACTIVE = 'Active'
        COMPLETED = 'Completed'

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    def __str__(self):
        return f"{self.student.username} -> {self.course.title}"
