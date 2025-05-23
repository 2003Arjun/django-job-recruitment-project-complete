# Django Recruit
A Recruitment project built with Django


# Tools & Services:
- Django : Python Web Framework
- Pytest: Testing Framework
- Celery: Task scheduling
- Flower: Task monitoring
- Redis: Celery broker


# Features

- Login
- Register
- Account verification
- Password reset
- Sending email
- Create/Update/Delete/List Job Adverts
- Apply to Jobs
- Track your applications and jobs
- Reject & Interview candidates
- Email notifications

# Running locally

Create a .env file by copying the .env.sample provided and run:


# Running In a VirtualEnv

Create a virtual environment using:
```
python3 -m venv venv
```

```
pip install -r requirements.txt
```

```
python manage.py makemigrations

python manage.py migrate
```

Run the server using:
```
python manage.py runserver
```

Celery worker
```
celery -A talent_base worker --loglevel=info
```
Flower dashboard
```
celery -A talent_base flower --ports=5555
```

# Run tests

Run tests in an activated virtualenv using:

```
pytest -v -rA
```





