# Generated by Django 5.0.7 on 2024-07-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
