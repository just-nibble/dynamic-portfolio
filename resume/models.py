from django.db import models

# Create your models here.


class Education(models.Model):
    insitution_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.CharField(max_length=100, blank=True, null=True)
    certficate = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.insitution_name)

    class Meta:
        ordering = ("-start_date",)


class Experience(models.Model):
    role = models.CharField(max_length=200, blank=True, null=True)
    institution_name = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    tasks = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.institution_name)

    class Meta:
        ordering = ("-start_date",)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        ordering = ("skill_name",)


class Interests(models.Model):
    Interest = models.TextField

    def __str__(self):
        return "interests"
