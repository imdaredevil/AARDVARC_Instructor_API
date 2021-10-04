from django.db import models
from .instructor import Instructor

class Active(models.IntegerChoices):
    ACTIVE = 1
    NOT_ACTIVE = 0
class LimitedEngagementEligible(models.IntegerChoices):
    ELIGIBLE = 1
    NOT_ELIGIBLE = 0


class InstructorAppointment(models.Model):
    type = models.IntegerField()
    active = models.SmallIntegerField(choices=Active.choices)
    vendorNumber = models.CharField(max_length=12, blank=True, default=True)
    homeDepartment = models.IntegerField()
    instructorId = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    fullTime = models.SmallIntegerField()
    tenureStatus = models.SmallIntegerField()
    title = models.CharField(max_length=300)
    limitedEngagementEligible = models.SmallIntegerField(choices=LimitedEngagementEligible.choices, default=LimitedEngagementEligible.NOT_ELIGIBLE)
    academicRank = models.CharField(max_length=100)

    def __str__(self):
        return self.title


