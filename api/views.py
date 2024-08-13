from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Import models
from students.models import Students
from classes.models import ClassPeriod
from teachers.models import Teacher
from courses.models import Courses
from classes.models import Classes  # Corrected import for ClassRoom

# Import serializers
from .serializer import TeacherSerializers
from .serializer import ClassPeriodSerializers
from .serializer import ClassRoomSerializers
from .serializer import StudentSerializers
from .serializer import CoursesSerializers

class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailsView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Students, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def enroll_student(self, student, course_id):
        course = get_object_or_404(Courses, id=course_id)
        student.courses.add(course)

    def post(self, request, id):
        student = get_object_or_404(Students, id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializers(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoursesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesDetailsView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Courses, id=id)
        serializer = CoursesSerializers(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = get_object_or_404(Courses, id=id)
        serializer = CoursesSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = get_object_or_404(Courses, id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeachersListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailsView(APIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassRoomListView(APIView):
    def get(self, request):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializers(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassRoomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassDetailsView(APIView):  # Renamed from Classes to ClassDetailsView
    def get(self, request, id):
        classroom = get_object_or_404(ClassRoom, id=id)  # Corrected reference
        serializer = ClassRoomSerializers(classroom)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = get_object_or_404(ClassRoom, id=id)  # Corrected reference
        serializer = ClassRoomSerializers(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = get_object_or_404(ClassRoom, id=id)  # Corrected reference
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassesPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializers(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailsView(APIView):
    def get(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializers(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializers(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)