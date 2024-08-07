from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField(primary_key = True)
    email = models.EmailField(max_length=30)
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=20)
    bio = models.TextField(max_length=250)
    pic = models.ImageField()
    

    def __str__(self):
        return f"{self.code},{self.first_name} - {self.class_name}"