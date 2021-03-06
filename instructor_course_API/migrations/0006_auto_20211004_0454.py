# Generated by Django 3.2.7 on 2021-10-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor_course_API', '0005_alter_course_templateid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='classCode',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='defaultEndTime',
            field=models.TimeField(blank=True, verbose_name='default end time'),
        ),
        migrations.AlterField(
            model_name='course',
            name='defaultStartTime',
            field=models.TimeField(blank=True, verbose_name='default start time'),
        ),
        migrations.AlterField(
            model_name='course',
            name='endDate',
            field=models.DateField(blank=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='startDate',
            field=models.DateField(blank=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='templateId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='eval',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Evaluator'), (0, 'Not Evaluator')]),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='USStatus',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='degree',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='instructorappointment',
            name='academicRank',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
