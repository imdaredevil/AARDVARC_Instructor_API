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

***Note:*** *In addition to the schema provided in the ER diagram, some fields can allowed to be left blank for easy creation of entries.* 

*For example, the field **officeHours** in the table **CourseInstructor** is a non NULL field. But, it can be left blank while creating entries since they are not useful for the API. If needed, they can be made as required fields*

### API Documentation

The swagger docs fot the API can be found by visiting http://localhost:8000/docs