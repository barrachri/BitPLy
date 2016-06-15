=====
Myblog
=====

Myblog is a simple demo of Django's basic usage.

Quick start
-----------

1. Add "myblog" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'myblog'
  }

2. Include the myblog URLconf in urls.py:
  url(r'^myblog/', include('myblog.urls'))

3. Run `python manage.py migrate` to create myblog's models.
3. Run `python manage.py makemigrations` to create myblog's models.
3. Run `python manage.py migrate` to create myblog's models.
3. Run `python manage.py create_fake_users 100` to create myblog's models.

PRODUCTION_ENV = True
DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = '2&e@x5svncf^t@20zpo*pl_utt2xogzy#s5@7o22dzf^&dx1a('
heroku config:set SECRET_KEY='2&e@x5svncf^t@20zpo*pl_utt2xogzy#s5@7o22dzf^&dx1a('

4. Run the development server and access http://127.0.0.1:8000/admin/ to
    manage blog posts.

5. Access http://127.0.0.1:8000/myblog/ to view a list of most recent posts.
