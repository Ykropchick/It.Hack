from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Student, Company, Project, Skill, Contact

# ...

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Contact)

# Register your models here.
