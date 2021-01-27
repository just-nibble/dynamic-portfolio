from django.db import models

# Create your models here.


class Education(models.Model):
    insitution_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.CharField()

    def __str__(self):
        return str(self.insitution_name)

    class Meta:
        ordering = "start_date"


class Experience(models.Model):
    insitution_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    tasks = models.TextField()
    start_date = models.DateField()
    end_date = models.CharField()

    def __str__(self):
        return str(self.insitution_name)

    class Meta:
        ordering = "start_date"


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        ordering = "skill_name"


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.hobby_name)

    class Meta:
        ordering = "hobby_name"
