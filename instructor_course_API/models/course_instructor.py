from django.db import models
from .course import Course
from .instructor_appointment import InstructorAppointment

class IsCoOrdinator(models.IntegerChoices):
        COORDINATOR = 0
        INSTRUCTOR = 1

class IsEval(models.IntegerChoices):
        EVALUATOR = 1
        NOT_EVALUATOR = 0

class CourseInstructor(models.Model):
    coord = models.SmallIntegerField(choices=IsCoOrdinator.choices)
    eval = models.SmallIntegerField(choices=IsEval.choices, blank=True)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructorId = models.ForeignKey(InstructorAppointment, on_delete=models.CASCADE)
    officeHours = models.TextField(blank=True)
    preferredContact = models.TextField(blank=True)
    def __str__(self):
        return self.courseId.title + "-" + self.instructorId.title
    