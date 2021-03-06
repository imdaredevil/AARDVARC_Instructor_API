from django.db import models
from django.db.models import F, Q

class isIrregularTime(models.IntegerChoices):
    IRREGULAR_TIME = 1
    REGULAR_TIME = 0

class AskCopy(models.IntegerChoices):
    IS_ASK_COPY = 1
    NOT_ASK_COPY = 0

class HasBeenEdited(models.IntegerChoices):
    EDITED = 1
    NOT_EDITED = 0

class UseCondensedSchedule(models.IntegerChoices):
    USE = 1
    NOT_USE = 0

class Course(models.Model):
    classCode = models.CharField(max_length=20, unique=True)
    courseNumber = models.CharField(max_length=8)
    section = models.IntegerField()
    title = models.CharField(max_length=100)
    units = models.SmallIntegerField()
    level = models.SmallIntegerField()
    startDate = models.DateField('start date', blank=True, null=True)
    endDate = models.DateField('end date', blank=True, null=True)
    defaultStartTime = models.TimeField('default start time', blank=True, null=True)
    defaultEndTime = models.TimeField('default end time', blank=True, null=True)
    irregularTimes = models.SmallIntegerField(choices=isIrregularTime.choices, default=isIrregularTime.REGULAR_TIME)
    dow = models.CharField(max_length=7)
    ohtime = models.TextField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    courseNotes = models.TextField(blank=True, default='')
    descriptionAssignment = models.TextField(blank=True)
    evalInfo = models.TextField(blank=True, default='')
    instructorBio = models.TextField(blank=True, default='')
    askCopy = models.SmallIntegerField(choices=AskCopy.choices, default=AskCopy.NOT_ASK_COPY)
    priorCourseId = models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank=True)
    programId = models.IntegerField() # since those tables are not present, foreign key is given as integer
    semesterId = models.IntegerField() # since those tables are not present, foreign key is given as integer 
    hasBeenEdited = models.SmallIntegerField(choices=HasBeenEdited.choices, default=HasBeenEdited.NOT_EDITED)    
    gradingBreakDown = models.TextField(blank=True, default='')
    useCondensedSchedule = models.SmallIntegerField(choices=UseCondensedSchedule.choices, default=UseCondensedSchedule.NOT_USE)
    templateId = models.IntegerField() # since those tables are not present, foreign key is given as integer
    extraFields = models.TextField(blank=True, default='')
    programYear = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(startDate__lte=F('endDate')),
                name='correct_date'
            ),
            models.CheckConstraint(
                check=Q(defaultStartTime__lte=F('defaultEndTime')),
                name='correct_time'
            ), 
        ] 
    def __str__(self):
        return self.classCode + "-" + self.title


    
    
    
    


     
    
    
    