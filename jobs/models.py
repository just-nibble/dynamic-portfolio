from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Job(models.Model):
    types = (
        ("web_apps", "web_apps"), ("api", "api"),
        ("upcoming", "upcoming")
    )
    job_name = models.CharField(max_length=100)
    job_type = models.CharField(
        choices=types, max_length=20,
        null=True, blank=True
    )
    job_link = models.URLField(null=True, blank=True)
    job_repo = models.URLField(null=True, blank=True)
    job_image = CloudinaryField("job_image", blank=True, null=True)
    job_description = models.CharField(max_length=100)
    technologies_used = models.CharField(max_length=200)

    def __str__(self):
        return str(self.job_name)

    class Meta:
        ordering = ("job_name",)


class Intro(models.Model):
    first_summary = models.CharField(max_length=400, blank=True, null=True)
    second_summary = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return "summary for portfolio"
