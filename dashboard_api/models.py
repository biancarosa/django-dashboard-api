from django.db import models

from django.contrib.auth.models import User
from django import db

class Settings(db.models.Model):
    COLORS = (
        (1, 'red'),
        (2, 'blue'),
        (3, 'green')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    preferred_color = db.models.IntegerField(choices=COLORS)