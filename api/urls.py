from django.urls import path
from .views import StudentListView, StudentDetailView
from .views import TeacherListView, TeacherDetailView
from .views import CoursesListView, CoursesDetailView
from .views import ClassesListView, ClassesDetailView
from .views import Class_PeriodListView, ClassPeriodDetailView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail_view"),
    
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    
    path("courses/", CoursesListView.as_view(), name="courses_list_view"),
    path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail_view"),
    
    path("classes/", ClassesListView.as_view(), name="classes_list_view"),
    path("classes/<int:pk>/", ClassesDetailView.as_view(), name="classes_detail_view"),
    
    path("class_periods/", Class_PeriodListView.as_view(), name="class_period_list_view"),
    path("class_periods/<int:pk>/", ClassPeriodDetailView.as_view(), name="classperiod_detail_view")
]