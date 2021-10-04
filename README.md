# AARDVARC Instructor Course API

## Local Setup

### Initial steps

- clone the repository
- cd AARDVARC_Instructor_API

### DB Migrations and Admin Management

Create and update database schema by running the migrations.
```bash
python manage.py migrate
```

Create superuser to access the admin portal.
```bash
python3 manage.py createsuperuser --email <email-id> --username <username>
```
The system will ask for password to be associated with this super user.

Run the server
```bash
python3 manage.py runserver
```

The admin portal can be accessed by visiting the URL http://localhost:8000/admin
The database tables can be populated using the admin portal. 

***Note:*** *In addition to the schema provided in the ER diagram, some fields are allowed to be left blank for easy creation of entries.* 

*For example, the field **officeHours** in the table **CourseInstructor** is a non NULL field. But, it can be left blank while creating entries since they are not useful for the API. If needed, they can be made as required fields*



https://user-images.githubusercontent.com/21989232/135854764-ffc7eb6a-9690-4ab2-acc0-6ab7e71d5b20.mp4



### API Documentation

The swagger docs fot the API can be found by visiting <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a>

**Auth Token**


https://user-images.githubusercontent.com/21989232/135856300-2ac70265-70a7-467e-a43c-a629cea6da30.mp4


**Courses**


https://user-images.githubusercontent.com/21989232/135856362-2819c3c9-e5ed-423b-88f9-472c37ca331f.mp4


The postman collection is also available in the name "AARDVARC_Instructor_API.postman_collection.json"
