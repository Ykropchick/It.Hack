from django.db import models
from django.conf import settings


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    value = models.CharField(max_length=40)


class UserProject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField()


class UserAuthentication(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.BigIntegerField()
    emailAddress = models.CharField(max_length=50)
    is_company = models.BooleanField()


class Company(models.Model):
    user = models.OneToOneField(
        UserAuthentication,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=40)
    description = models.TextField()
    photo = models.ImageField()


class User(models.Model):
    user = models.OneToOneField(
        UserAuthentication,
        on_delete=models.CASCADE
    )
    frst_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    photo = models.ImageField()
    sills = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    course = models.IntegerField()
    specialization = models.CharField(max_length=40)
    university = models.CharField(max_length=40)
    contacts = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE
    )
    is_authorised = models.BooleanField()
    projects = models.ForeignKey(
        UserProject,
        on_delete=models.CASCADE
    )
