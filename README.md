# Quarantine Student Task Manager - Backend

## Official Frontend README  
[Main README](https://github.com/python-final-project/quarantine-student-task-manager/blob/staging/README.md)  

## Overview  
Application to help parents manage their children's homework, websites, and associated passwords.

This is the backend for the Quarantine Student Task Manager. It's a django backend utilizing the built-in sqllite database.

---

## Installation  

1. Git clone qstm-backend repo  
2. CD into qstm-backend and run `poetry install`  
3. Run `poetry shell` to enter virtual environment  
4. Create your version of the `.env` file and add it to the qstm directory(sibling to `settings.py`)  
5. From the root, you can run `python manage.py runserver`  

This will install, and get this backend running locally. To run within a docker container do these additional steps:  
- Dockerfile and docker-compose.yml are provided. To ensure requirements.txt is up-to-date from the root run `poetry export -f requirements.txt -o requirements.txt`.  
- Then if you have docker installed locally, you can run `docker-compose up --build` either detached or not with the `-d` flag.  


## Dependencies  
python = "~3.8"  
djangorestframework = "^3.11.0"  
whitenoise = "^5.1.0"  
django-cors-headers = "^3.4.0"  
djangorestframework_simplejwt = "^4.4.0"  
psycopg2-binary = "^2.8.5"  
gunicorn = "^20.0.4"  
django-environ = "^0.4.5"  

---

## Authors  
- Software Developer: Joseph Zabaleta
  - [Official Github](https://github.com/joseph-zabaleta)  
- Software Developer: Jesse Pena
  - [Official Github](https://github.com/jpchato)  
- Software Developer: Iris Leal
  - [Official Github](https://github.com/ilealm)  

---

## License  
This project is under the MIT License.

---

## Acknowledgements / Resources / Inspiration Links 
- none

---

## Version History  
- 1.0.0 20200713
  - Initial backend files were created 20200713  
  - Created qstm app
  - Created user, parent, student, task, and site models to represent our domain model.
  - Updated settings.py to include the use of environment file  
  - Added docker files to use backend in a container  
  - Deployed first version of working API to aws

