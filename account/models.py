from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = CloudinaryField('portfolio_image')
