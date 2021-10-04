from django.db import models

class Instructor(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, default='',blank=True)
    email = models.CharField(max_length=254, unique=True)
    phone = models.CharField(max_length=30)
    photo = models.CharField(max_length=100,blank=True,default='')
    office = models.CharField(max_length=100, blank=True, default='')
    USStatus = models.SmallIntegerField(null=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True,default='')
    cityStateZip = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    degree = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName
    