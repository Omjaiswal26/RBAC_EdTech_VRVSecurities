
# RBAC EdTech Platform

Django REST Framework based Backend for EdTech platform demonstrating RBAC with following roles:
- Student
- Teacher
- Admin

Swagger URL: http://127.0.0.1:8000/swagger/  
Postman Collection: https://www.postman.com/clinibooth/workspace/omjaiswal-vrv



# Past Experience with RBAC

1. Set up entire backend for a client as a freelance backend developer. Implemented central authentication with 3 roles: Patient, Doctor and Admin. Restricted access using custom permissions validating request.user.role against allowed role.  
Proof: https://www.upwork.com/freelancers/~010196aaff7de662c1?viewMode=1

2. Implemented RBAC with roles Visitor, Contributor and Admin for a Freelance Travel Website Project.
Proof: https://www.upwork.com/freelancers/~010196aaff7de662c1?viewMode=1


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