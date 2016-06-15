from datetime import datetime, timezone
import requests

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from main import models

# Url of the API to generate random users
URL_RANDOM_USER = "http://api.randomuser.me/1.0/?results={}&inc=name,email,login,registered,picture"

class Command(BaseCommand):
    '''Helper to create fake users inside the database, accepts 1 parameter,
    an integer for the number of users'''

    help = 'Creates random users inside the database, accepts 1 parameter (number of users)'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int)

    def handle(self, *args, **options):
        # Do a GET request to the api
        r = requests.get(URL_RANDOM_USER.format(options['num_users']))

        # Check is the status code is equal to 200
        if r.status_code == 200:

            # Loads the json from the get request
            json = r.json()

            # Check if there is some error inside the json
            # If yes prints the error in the console
            if "error" in json:
                self.stdout.write(self.style.ERROR(json['error']))
            else:
                users = json['results']

                # Create and save a new user object for every entry inside the json from the api
                for user in users:
                    new_user = User.objects.create_user(username = user['login']['username'],
                    password = user['login']['password'],
                    first_name = user['name']['first'],
                    last_name = user['name']['last'],
                    email = user['email'],
                    date_joined = datetime.fromtimestamp(user['registered'], timezone.utc)
                    )
                    # Save the personal User thumbnail inside UserImage
                    p= models.UserImage.objects.create(image_url= user['picture']['medium'], user=new_user)
                    print(p)
            self.stdout.write(self.style.SUCCESS('Successfully inserted {} users from randomuser.me'.format(options['num_users'])))
