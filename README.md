# ben12-desktop-app
Desktop app for the project integration course of year 2 quarter 3-4 from Saxion.

To use:
- Make sure to have Python installed (the app is tested with Python 3.10)
- navigate to the top ben12server directory (name is subject to change)
- run `pip install -r requirements.txt`
- in your console, type: `py manage.py runserver`
- in your browser, navigate to <a>127.0.0.1:8000/app</a>

To update database models:
1. Change ben12app/models.py
2. run `py manage.py makemigrations ben12app`
3. run `py manage.py migrate`

To view API documentation:
1. run `py manage.py runserver`
2. navigate to <a>127.0.0.1:8000/swagger-ui</a>