import os
from random import choice, randint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()
from api.models import *
from datetime import date
from dateutil.relativedelta import relativedelta

from faker import Faker
from faker.providers import internet, job, company, color, date_time
import faker

f = Faker("RU_ru")
f.add_provider(internet)
f.add_provider(job)
f.add_provider(company)
f.add_provider(color)
f.add_provider(date_time)


for x in range(20):
    f_name = f.first_name()
    l_name = f.last_name()
    description = ' '.join([f.word() for q in range(10)])
    course = randint(1, 4)
    uni = choice(["ITMO", "SPBGU", "UNECON", "GUAP", "HSE"])
    spec = f.job()
    auth = 1

    student = Student(
        first_name=f_name,
        last_name=l_name,
        description=description,
        course=course,
        university=uni,
        specialization=spec,
        is_authorised=auth
    )
    # print(student.pk)
    # exit(0)
    student.save(force_insert=True)
    student = Student.objects.all().filter(first_name=f_name).filter(last_name=l_name)[0]
    # print(student.id)
    con1 = Contact(owner=student, type="telephone", value=f.phone_number())
    con1.save(force_insert=True)
    con2 = Contact(owner=student, type="email", value=f.free_email())
    con2.save(force_insert=True)

for i in range(20):
    name = f.company()
    description = ' '.join([f.word() for _ in range(20)])
    c = Company(
        name=name,
        description=description
    )
    c.save()
    c = Company.objects.filter(name=name, description=description)[0]
    d = ' '.join([f.word() for _ in range(10)])
    s_desc = ' '.join(description.split()[:3])
    p1 = Project(
        owner=c,
        name=f.color_name(),
        description=d,
        date=date.today() + relativedelta(months=randint(1, 4), days=randint(1, 31)),
        short_description=s_desc

    )
    p1.save()


