from django.db import models

from django.contrib.auth.models import User
from django.db import models as django_models

class Settings(django_models.Model):
    COLORS = (
        (1, 'red'),
        (2, 'blue'),
        (3, 'green')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    preferred_color = django_models.IntegerField(choices=COLORS)