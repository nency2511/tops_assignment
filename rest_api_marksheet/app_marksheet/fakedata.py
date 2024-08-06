from faker import Faker
fake = Faker()
from .models import *
import random


def setmarks():

    students = Student.objects.all()
    for std in students:
        subjects = Subject.objects.all()
        for sub in subjects:
            StudentMark.objects.create(
                student=std,
                subject=sub,
                marks=random.randint(0,100)
            )

def setdata(n=10):
    for i in range(n):
        dept_data = Department.objects.all() #get obj
        r_index = random.randint(0, len(dept_data)-1)
        dept = dept_data[r_index]
        name= fake.name()
        email = fake.email()

        student_id = f'21064010_{random.randint(100,999)}'
        student_id_obj = StudentId.objects.create(student_id=student_id) #get obj


        Student.objects.create(name = name,
        email=email,
        department=dept,
        student_id=student_id_obj
        )