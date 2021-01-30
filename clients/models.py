from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

# Create your models here.


class Client(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = CloudinaryField(
        'portfolio_image/profile_pic',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
