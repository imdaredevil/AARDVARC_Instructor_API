# Generated by Django 3.2.7 on 2021-10-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor_course_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='askCopy',
            field=models.SmallIntegerField(choices=[(1, 'Is Ask Copy'), (0, 'Not Ask Copy')], default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseNotes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='descriptionAssignment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='evalInfo',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='extraFields',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='gradingBreakDown',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='hasBeenEdited',
            field=models.SmallIntegerField(choices=[(1, 'Edited'), (0, 'Not Edited')], default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructorBio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='irregularTimes',
            field=models.SmallIntegerField(choices=[(1, 'Irregular Time'), (0, 'Regular Time')], default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='ohtime',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='priorCourseId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='programYear',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='course',
            name='templateId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='useCondensedSchedule',
            field=models.SmallIntegerField(choices=[(1, 'Use'), (0, 'Not Use')], default=0),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='eval',
            field=models.SmallIntegerField(choices=[(1, 'Evaluator'), (0, 'Not Evaluator')], default=0),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='officeHours',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='preferredContact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='middleName',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='office',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='instructorappointment',
            name='limitedEngagementEligible',
            field=models.SmallIntegerField(choices=[(1, 'Eligible'), (0, 'Not Eligible')], default=0),
        ),
        migrations.AlterField(
            model_name='instructorappointment',
            name='type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='instructorappointment',
            name='vendorNumber',
            field=models.CharField(blank=True, default=True, max_length=12),
        ),
    ]
