from django.db import models
from student.models import Student

class Courses(models.Model):
    course_title = models.CharField(max_length = 20)
    course_category = models.CharField (max_length = 20)
    course_start_date = models.DateField ()
    course_end_date = models.DateField ()
    course_code = models.PositiveSmallIntegerField ()
    teacher_code = models.PositiveSmallIntegerField ()
    student_code = models.PositiveSmallIntegerField ()
    student_number = models.PositiveSmallIntegerField ()
    course_fee = models.PositiveSmallIntegerField ()
    student_code=models.ForeignKey(Student, on_delete=models.CASCADE, related_name = 'courses')


    def __str__(self):
        return f"{self.course_title}"