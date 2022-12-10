import os
from random import choice, randint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()
from api.models import *

from faker import Faker
from faker.providers import internet, job, company, color
import faker

f = Faker("RU_ru")
f.add_provider(internet)
f.add_provider(job)
f.add_provider(company)
f.add_provider(color)


for x in range(20):
    f_name = f.first_name()
    l_name = f.last_name()
    description = ' '.join([f.word() for x in range(10)])
    course = randint(1, 4)
    uni = choice(["ITMO", "SPBGU", "UNECON", "GUAP", "HSE"])
    spec = f.job()
    auth = 1

    c = Student(
        first_name=f_name,
        last_name=l_name,
        description=description,
        course=course,
        university=uni,
        specialization=spec,
        is_authorised=auth,
    )
    c.save()
    con1 = Contact(owner=c, type="telephone", value=f.phone_number())
    con2 = Contact(owner=c, type="email", value=f.free_email())
    con1.save()
    con2.save()

for i in range(20):
    name = f.company()
    description = ' '.join([f.word() for x in range(20)])
    c = Company(name=name, description=description)
    c.save()
    p1 = Project(owner=c, )

