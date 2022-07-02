from django.db import models
from django.contrib.auth.models import User,AbstractUser


class MyUser(AbstractUser):
    student_name = models.CharField(max_length=30)
    collegeid = models.CharField(max_length=30)
    dept_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)



class Departments(models.Model):
    dept_name = models.CharField(max_length=30)
    dept_hod = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)


    def __str__(self):
        return self.dept_name





