
# RBAC EdTech Platform

Django REST Framework based Backend for EdTech platform demonstrating RBAC with following roles:
- Student
- Teacher
- Admin

Swagger URL: 127.0.0.1:8000\swagger\
Postman Collection: 


# Run Locally

1. Create a virtual env : 
    python -m venv env
2. Install dependencies: 
    pip install -r requirements.txt
3. Run Makemigrations and Migrate commands
    python manage.py makemigrations
    python manage.py migrate
4. Run server
    python manage.py runserver