=====
BitPLy
=====

This is a super cool copy cat of a service like Bitly

Test before run !

python manage.py test

**Python version used: 3.x**

**Check your ENV_VAR if you want a local env or a production env**

Quick start Local
-----------

1. Run 'pip install requirements/dev.txt'
2. Run 'python manage.py makemigrations'
3. Run 'python manage.py migrate'
4. Run 'python manage.py create_fake_users 100'
5. Run the development server and access http://127.0.0.1:8000

Quick start Heroku
-----------
1. Run 'heroku create'
2. Run 'heroku config:set PRODUCTION_ENV=True' to set ENV_VAR
3. Run 'heroku config:set SECRET_KEY='PutYourSecretKeyHere''
4. Run 'git push heroku master'
5. Run 'heroku run python manage.py migrate'
6. Run 'heroku run python manage.py create_fake_users 100'
7. Access the heroku url
