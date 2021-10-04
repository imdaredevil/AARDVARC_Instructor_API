from django.contrib import admin

from .models import Course, CourseInstructor, Instructor, InstructorAppointment

admin.site.register(Course)
admin.site.register(CourseInstructor)
admin.site.register(Instructor)
admin.site.register(InstructorAppointment)

# Register your models here.
