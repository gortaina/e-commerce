from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

#Herda o usuário do django
class User(AbstractUser):
    pass
