# Generated by Django 3.2.7 on 2021-10-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor_course_API', '0007_auto_20211004_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ohtime',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='officeHours',
            field=models.TextField(),
        ),
    ]
