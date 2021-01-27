from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Job(models.Model):
    job_name = models.CharField(max_length=100)
    job_link = models.URLField(null=True, blank=True)
    job_repo = models.URLField(null=True, blank=True)
    job_image = CloudinaryField("job_image", blank=True, null=True)
    job_description = models.CharField(max_length=100)
    technologies_used = models.CharField(max_length=200)

    def __str__(self):
        return str(self.job_name)

    class Meta:
        ordering = "job_name"
