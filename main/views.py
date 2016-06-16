import string
import random
from math import floor

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from main import models

def random_generator(min=3, max=settings.SHORT_URL_MAX_LEN,
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    '''Just a stupid (pseudo) random generator of a string,
    has a min lenght and a max lenght, chars is where the
    random chars are extracted'''

    r = random.randint(min, max)
    return ''.join(random.choice(chars) for x in range(r))

class Index(View):
    ''''''

    def get(self, request):
        # Index page of the website
        form = models.UrlForm()
        return render(request, "index.html", {"form": form})

    def post(self, request):
        #aggiungere un check se l'url esiste
        # aggiungere un check se la short url esiste
        form = models.UrlForm(request.POST)
        if form.is_valid():

            while True:
                short_url = random_generator()
                new = not(models.Url.objects.filter(short_url=short_url).exists())
                if new is True:
                    break
            user_id_list = User.objects.values_list('id', flat=True)
            random_user =  random.choice(user_id_list)
            obj_url, created = models.Url.objects.get_or_create(url=form.cleaned_data['url'], defaults={
           "short_url" : short_url,
           "created_by": User.objects.get(pk=random_user)
           })
            long_url = request.build_absolute_uri(obj_url.short_url)
            return render(request, "new_url.html", {"token": obj_url.short_url, "long_url": long_url})
        else:
            print(form.errors['url'].as_json())
            return render(request, "index.html", {"form": form})

class RedirectToUrl(View):
    ''''''
    def get(self, request, short_url):
        try:
            url = models.Url.objects.get(short_url=short_url)
            return redirect(url.url)
        except ObjectDoesNotExist:
            return render(request, "error.html", {"short_url": short_url})

class UrlInfo(View):
    ''''''
    def get(self, request, short_url):
        try:

            obj_url = models.Url.objects.get(short_url=short_url)
            image = models.UserImage.objects.get(user=obj_url.created_by)
            long_url = request.build_absolute_uri(obj_url.short_url)

            return render(request, "urlinfo.html", {
            'url': obj_url, "image" : image, "long_url": long_url
        })
        except ObjectDoesNotExist:
            return render(request, "error.html", {"short_url": short_url})
