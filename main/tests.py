from datetime import datetime, timezone

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from main.models import UserImage, Url
from main.views import random_generator

class UserTestCase(TestCase):
    """Test User model"""
    @classmethod
    def setUp(self):
        User.objects.create_user(username = "PincoPallino",
        password = "10clouds",
        first_name = "Pinco",
        last_name = "Pallino",
        email = "pinco@pallino.com",
        date_joined = datetime.now(timezone.utc)
        )
        User.objects.create_user(username = "GiulioCesare",
        password = "poland",
        first_name = "Giulio",
        last_name = "Cesare",
        email = "giulio@cesare.com",
        date_joined = datetime.now(timezone.utc)
        )

    def test_user(self):
        user1 = User.objects.get(username="PincoPallino")
        user2 = User.objects.get(username="GiulioCesare")
        self.assertEqual(user1.email, 'pinco@pallino.com')
        self.assertEqual(user2.email, 'giulio@cesare.com')

class UserImageTestCase(TestCase):
    """Test UserImage model"""
    def setUp(self):
        UserTestCase.setUp()
        self.user1 = User.objects.get(username="PincoPallino")
        self.user2 = User.objects.get(username="GiulioCesare")
        user_image_1 = UserImage.objects.create(image_url="http://www.example1.com", user=self.user1)
        user_image_2 = UserImage.objects.create(image_url="http://www.example2.com", user=self.user2)

    def test_user_image(self):
        user_image_1 = UserImage.objects.get(user=self.user1)
        user_image_2 = UserImage.objects.get(user=self.user2)
        self.assertEqual(user_image_1.image_url, 'http://www.example1.com')
        self.assertEqual(user_image_2.image_url, 'http://www.example2.com')

class UrlTestCase(TestCase):
    """Test Url model"""
    def setUp(self):
        UserTestCase.setUp()
        user1 = User.objects.get(username="PincoPallino")
        user2 = User.objects.get(username="GiulioCesare")
        self.token_1 = random_generator()
        self.token_2 = random_generator()
        url_1 = Url.objects.create(url="http://www.example1.com", short_url=self.token_1, created_by=user1)
        url_2 = Url.objects.create(url="http://www.example2.com", short_url=self.token_2, created_by=user2)

    def test_url(self):
        url_1 = Url.objects.get(short_url=self.token_1)
        url_2 = Url.objects.get(short_url=self.token_2)
        self.assertEqual(url_1.url, 'http://www.example1.com')
        self.assertEqual(url_2.url, 'http://www.example2.com')

class ViewTestCase(TestCase):
    """Test Views"""
    def setUp(self):
        self.c = Client()
        UserTestCase.setUp()
        user = User.objects.get(username="PincoPallino")
        token = random_generator()
        self.test_url = "http://www.example1.com"
        self.url = Url.objects.create(url=self.test_url, short_url=token, created_by=user)

    def test_index(self):
        """Test Index View"""
        response = self.c.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_post_index(self):
        """Test url creation"""
        test_url = 'https://www.google.pl'
        response = self.c.post(reverse("index"), {'url': test_url})
        url = Url.objects.get(url=test_url)
        self.assertEqual(url.url, test_url)

    def test_post_empty(self):
        """Test index form empty"""
        response = self.c.post(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'url', ['This field is required.'])

    def test_post_empy(self):
        """Test index form error"""
        response = self.c.post(reverse("index"), {'url': "test_url"})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'url', ['Enter a valid URL.'])

    def test_url_info(self):
        """Test UrlInfo View"""
        response = self.c.get(reverse("url_info", kwargs={'short_url': self.url.short_url}))
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_url(self):
        """Test RedirectToUrl View"""
        response = self.c.get(reverse("redirect_to_url", kwargs={'short_url': self.url.short_url}))
        self.assertEqual(response.url, self.test_url)

    def test_404(self):
        """Test 404 error"""
        response = self.c.get('/ERROR/ERROR')
        self.assertEqual(response.status_code, 404)
