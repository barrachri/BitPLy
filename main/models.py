from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class UserImage(models.Model):
    '''This model is used to save the url of the personal thumbnail'''
    image_url = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.image_url, self.user.username)

class Url(models.Model):
    '''This model is used to save the information about the short version of the url
    url and short_url are set unique=True to reinforce the constraint at a db level'''
    url = models.URLField(unique=True)
    short_url = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url

    def validate_unique(self, exclude):
        '''This is method is overrid in a Naive way,
        both uniqueness of url and short_url are checked in the views'''
        pass

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url']
