# Generated by Django 5.0.7 on 2024-07-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_duration', models.DateField()),
                ('students', models.PositiveSmallIntegerField()),
                ('class_training_assistant', models.CharField(max_length=20)),
                ('class_representatives', models.TextField()),
                ('teacher_code', models.PositiveSmallIntegerField()),
                ('number_of_whiteboards', models.PositiveSmallIntegerField()),
                ('number_of_TVs', models.PositiveSmallIntegerField()),
                ('number_of_desks', models.PositiveSmallIntegerField()),
                ('number_of_chairs', models.PositiveSmallIntegerField()),
                ('class_code', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
