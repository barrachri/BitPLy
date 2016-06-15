=====
BitPLy
=====

This is a super cool copy cat of a service like Bitly

Quick start Local
-----------

1. Check your ENV_VAR if you want a local env or a production env
3. Run 'python manage.py makemigrations main'
4. Run 'python manage.py migrate'
5. Run 'python manage.py create_fake_users 100'
6. Run the development server and access http://127.0.0.1:8000

Quick start Heroku
-----------
1. Run 'heroku config:set PRODUCTION_ENV=True' to set ENV_VAR
2. Run 'heroku config:set SECRET_KEY='PutYourSecretKeyHere'
3. Run 'heroku create'
4. Run 'git push heroku master'
6. Run 'heroku run python python manage.py makemigrations main'
7. Run 'heroku run python python manage.py migrate'
8. Run 'heroku run python python manage.py create_fake_users 100'
9. Access the heroku url
