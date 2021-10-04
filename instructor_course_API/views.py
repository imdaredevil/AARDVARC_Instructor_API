
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from AARDVARC.accounts.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import Instructor
from rest_framework.authtoken.models import Token



class InstructorCourseView(viewsets.ViewSet):
    """
    returns the course codes for all the active appointments for the given instructor
    While calling it from another service ( eg. Postman ) use bearer token authentication.
    The token can be obtained by the Token API with user name and client secret provided to you by the admin
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [ExpiringTokenAuthentication, SessionAuthentication]
    def list(self, request, format=None):
        """
        returns the course codes for all the active appointments for the given instructor
        While calling it from another service ( eg. Postman ) use bearer token authentication.
        The token can be obtained by the Token API with user name and client secret provided to you by the admin
        """
        instructor_email = request.GET.get("email")
        if not instructor_email:
            return Response({
                "error": "email not given",
            }, status=400)
        else:
            instructor = Instructor.objects.get(email = instructor_email)
            if (not instructor):
                return Response({
                    "error": "instructor not found"
                },status=404) 
            instructor_appointments = instructor.instructorappointment_set.filter(active = 1)
            if not instructor_appointments or len(instructor_appointments) == 0:
                return Response({
                    "error": "No instructor appointments for given instructor"
                })
            result = []
            for instructor_appointment in instructor_appointments:
                course_instructors = instructor_appointment.courseinstructor_set.all()
                result.extend([{ "classCode" : course_instructor.courseId.classCode } for course_instructor in course_instructors])
            return Response(result)

class AuthView(viewsets.ViewSet):
    """
    returns dummy text for basic auth
    """
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request, format=None):
        print(request.user.id)
        print()
        token = Token.objects.filter(user = request.user.id)
        if len(token) > 0:
            token[0].delete()
        token = Token(user=request.user)
        token.save()
        return Response( { "token": str(token) })     

