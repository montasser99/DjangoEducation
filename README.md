# DjangoRducation
## Overview
DjangoEducation is an online course management platform, developed with Django, Python, and Sqlite3, that enables teachers to create and manage course content, track student progress, and foster engagement. It includes AI-driven features to enhance the learning experience.

# Projet Django - Installation Guide

## Étapes d'installation

### 1. Clone the Repository
To get started, clone the project using the following command:
``` 
https://github.com/montasser99/DjangoEducation.git
```

### 2.Set Up Project Folder and Virtual Environment
Create a new directory for the project, move into it, and set up a virtual environment:
``` 
mkdir DjangoEducation
cd DjangoEducation
virtualenv djangoEnv
```

### 3. Activate the Virtual Environment
Activate the virtual environment with this command:
``` 
djangoEnv\Scripts\activate
```

### 4. Install Django
While the environment is activated, install Django version 4.2:
``` 
python -m pip install django==4.2

```
### 5. Navigate to Project Folder and Apply Migrations
Move into the cloned project folder and generate and apply migrations:
``` 
cd ../Django-authentification-master/DjangoEducation
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
Create a superuser account to access the admin dashboard:
```
python manage.py createsuperuser
```
### 7. Start the Server
``` 
python manage.py runserver
```
## Support 
If you encounter any issues, feel free to contact:
**Montasser Benouirane**

Email: montasser.benouirane@esprit.tn

## Application Overview and Visuals

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/a272db50-073c-4b8e-8dd7-bb2b89f9143d" alt="Image 1" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/a1775e3d-300a-4357-8961-cbf8d1c02a83" alt="Image 2" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/e859c592-e5a4-406c-bb12-159453500373" alt="Image 3" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/d42441ee-96a0-4d68-a830-fe35014f4d06" alt="Image 4" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/779e2353-e310-4181-b75f-ca90a0e60053" alt="Image 5" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/5d381eeb-5c0d-4e2e-ba25-922fd9d48146" alt="Image 6" style="height: 150px; margin: 0.5%;">
  <img src="https://github.com/user-attachments/assets/04812033-f174-4830-a3db-5b38cbb671bf" alt="Image 7" style="height: 150px; margin: 0.5%;">
</div>






