# Generated by Django 5.0.7 on 2024-07-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_bio_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
