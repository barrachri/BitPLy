import string
import random

from django.conf import settings


def random_generator(min=3, max=settings.SHORT_URL_MAX_LEN,
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    '''Just a stupid (pseudo) random generator of a string,
    has a min lenght and a max lenght, chars is where the
    random chars are extracted'''

    r = random.randint(min, max)
    return ''.join(random.choice(chars) for x in range(r))
