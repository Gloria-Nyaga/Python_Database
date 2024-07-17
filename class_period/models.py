from django.db import models


class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=20)
    attendance_count = models.SmallIntegerField()
    period_title = models.CharField(max_length=20)
    period_description = models.TextField()
    students_limit = models.SmallIntegerField()

 
    def __str__(self):
       return f"{self.classroom} {self.end_time}"   

 