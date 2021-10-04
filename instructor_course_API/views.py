
from datetime import timedelta
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from AARDVARC.accounts.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import BasicAuthentication
from .models import Instructor, IsCoOrdinator
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
import traceback



class InstructorCourseView(viewsets.ViewSet):
    """
    Returns the **course codes** for all the **active appointments** for the given **instructor**
    
     - The request must be authenticated using bearer token ( Authorization: "Bearer <token>")
     - The token can be obtained by the Token API
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [ExpiringTokenAuthentication]
    @extend_schema(
        parameters=[
          OpenApiParameter(name="email", 
                           type=OpenApiTypes.STR,
                           description="the email of the instructor",
                           required=True),
        ],
        responses={
            200: OpenApiResponse(description="""
            The courses for the given instructor are returned in JSON format.
            The data field in the response JSON contains an array of objects
            each of which represents a course and has the following fields
            {
                "course_code" : course code to generate the link,
                "start_date" : start date of the course,
                "end_date" : end date of the course,
                "start_time": default start time of the course,
                "end_time": default end time of the course
                "location": location of the course
                "description": description of the course  
                "program": program which the course belong to
                "semester": semester in which the course in handled
                "appointment_title": the title of the instructor's appointment
                "instructor_role": tells whether, the instructor role is "instructor" or "co-ordinator"
                "office_hours": the office hours of the instructor for the course
            }
            """), 
            401: OpenApiResponse(description="invalid token or the token is expired"),
            400: OpenApiResponse(description="The email is not given as parameter"), 
            404: OpenApiResponse(description="Instructor or instructor appointments not found") 
        })
    def list(self, request, format=None):
        try:
            instructor_email = request.GET.get("email")
            if not instructor_email:
                return Response({
                    "error": "email not given",
                }, status=400)
            else:
                instructors = Instructor.objects.filter(email = instructor_email)
                if (not instructors) or len(instructors) == 0:
                    return Response({
                        "error": "instructor not found"
                    },status=404) 
                instructor = instructors[0]
                instructor_appointments = instructor.instructorappointment_set.filter(active = 1)
                if not instructor_appointments or len(instructor_appointments) == 0:
                    return Response({
                        "error": "No instructor appointments for given instructor"
                    })
                result = []
                for instructor_appointment in instructor_appointments:
                    course_instructors = instructor_appointment.courseinstructor_set.all()
                    for course_instructor in course_instructors:
                        course = course_instructor.courseId
                        instructor_role = 'Instructor'
                        if course_instructor.coord == IsCoOrdinator.COORDINATOR:
                            instructor_role = 'Coordinator'
                        result.append({
                            "course_code" : course.classCode,
                            "start_date" : course.startDate,
                            "end_date" : course.endDate,
                            "start_time": course.defaultStartTime,
                            "end_time": course.defaultEndTime,
                            "location": course.location,
                            "description": course.description, 
                            "program": course.programId,
                            "semester": course.semesterId,
                            "appointment_title": instructor_appointment.title,
                            "instructor_role": instructor_role, 
                            "office_hours": course_instructor.officeHours
                     })
                return Response(result)
        except:
                return Response({"error" : traceback.print_exc() }, status=500)



class AuthView(viewsets.ViewSet):
    """
    Generates **a bearer token** for the user.

    *The request must be authenticated with BasicAuthentication with the given username and password from the admin*
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes =  [BasicAuthentication]
    @extend_schema(
        parameters=[],
        responses={
            200: OpenApiResponse(description="The token is returned"), 
            401: OpenApiResponse(description="invalid username or password"), 
        })
    def list(self, request, format=None):
        try:
            token = Token.objects.filter(user = request.user.id)
            if len(token) > 0:
                token[0].delete()
            token = Token(user=request.user)
            token.save()
            return Response( { 
                "token": str(token),
                "expires_in": 3600,
                }) 
        except:
                return Response({"error" : traceback.print_exc() }, status=500)    

