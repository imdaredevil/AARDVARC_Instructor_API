# Generated by Django 3.2.7 on 2021-10-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor_course_API', '0004_alter_course_priorcourseid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='templateId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
