from django.db import models
from django.conf import settings


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    photo = models.ImageField(null=True)

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(
        Company,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField()
class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    photo = models.ImageField(null=True)
    description = models.TextField(null=True)
    course = models.IntegerField(null=True)
    specialization = models.CharField(max_length=40, null=True)
    university = models.CharField(max_length=40, null=True)
    is_authorised = models.BooleanField(null=True)
    skills = models.ManyToManyField(
        Skill,
        blank=True
    )


class Contact(models.Model):
    owner = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        default=None
    )
    type = models.CharField(max_length=40)
    value = models.CharField(max_length=40)


