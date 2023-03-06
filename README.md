
# Florens 

This is a REST API for an activity management application for nurses. The API is built with Django and Django Rest Framework, and uses PostgreSQL as the database manager. The application allows nurses to manage their work shift schedules, see patient medical history, inventory control, follow up on care plans, and calculate doses of medication for patients.

### Technologies Used

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)    



Requirements
------------

-  Python 3.11.0
-  Django 4.1.5
-  Django REST Framework 3.14.0
-  psycopg2 2.9.5

## Getting Started


To run the application, follow these steps:

**Clone the repository**
```bash
  git clone https://github.com/greghades/florens_backend.git
```

**Install the required dependencies by running**
```bash
 pip install -r requirements.txt
```
**Create a PostgreSQL database and configure the settings in settings.py with environment variables**
```bash
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}
```
**Run the migrations by running** 
 ```bash
 python manage.py migrate
```
**Start the development server by running**
 ```bash
python manage.py runserver
```
   

API Endpoints

    /api/doc/: Endpoint with all endpoints in swagger
    /api/redoc/: Other view  with all endpoints in swagger


Contributing

Contributions are welcome! Please open an issue or pull request for any changes or bug fixes.
License

This project is licensed under the MIT License - see the LICENSE file for details.
