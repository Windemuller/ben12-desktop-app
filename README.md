# ben12-desktop-app
Desktop app for the project integration course of year 2 quarter 3-4 from Saxion.

To use:
- Make sure to have Python installed (the app is tested with Python 3.10)
- Install the Django framework with `pip install django`
- Install the Django Rest Framework with `pip install django_rest_framework`
- navigate in your console to the top ben12server folder (name is subject to change)
- in your console, type: `py manage.py runserver`
- in your browser, navigate to <a>127.0.0.1:8000/app</a>

To update database models:
1. Change ben12app/models.py
2. run `py manage.py makemigrations ben12app`
3. run `py manage.py migrate`