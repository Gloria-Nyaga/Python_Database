# Generated by Django 5.0.7 on 2024-07-17 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course_title',
        ),
    ]