from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from teacher.models import Teacher
from courses.models import Courses
from classes.models import Classes
from class_period.models import ClassPeriod

from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import CoursesSerializer
from .serializers import ClassesSerializer
from .serializers import ClassPeriodSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    
class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    
class Class_PeriodListView(APIView):
    def get(self, request):
        periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(periods, many=True)
        return Response(serializer.data)