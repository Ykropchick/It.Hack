import os
from random import choice, randint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()
from api.models import *

from faker import Faker
from faker.providers import internet, job
import faker

f = Faker("RU_ru")
f.add_provider(internet)


for x in range(20):
    f_name = f.first_name()
    l_name = f.last_name()
    description = ' '.join([f.word() for x in range(10)])
    course = randint(1, 4)
    uni = choice(["ITMO", "SPBGU", "UNECON", "GUAP", "HSE"])
    spec = f.job()
    auth = 1
    con1 = Contact(id=x, type="telephone", value=f.phone_number())
    con1.save()
    c = Student(
        first_name=f_name,
        last_name=l_name,
        description=description,
        course=course,
        university=uni,
        specialization=spec,
        is_authorised=auth,
        contacts=con1
    )
    c.save()
