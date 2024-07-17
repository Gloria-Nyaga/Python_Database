from django.db import models
from student.models import Student

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField(default=0)  
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    salary = models.BigIntegerField()
    hire_date = models.DateTimeField()
    course = models.CharField(max_length=20, default='python')
    gender = models.CharField(max_length=10)
    bio = models.TextField()
    profile = models.ImageField()
    course_code= models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}, {self.code}"