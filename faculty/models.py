from django.db import models
from django.utils import timezone



class Department(models.Model):
    name = models.CharField(max_length=150)
    head = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    description = models.TextField()
    head_name = models.CharField(max_length=150)
    head_contact = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    lessons_list = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    def __str__(self):
        return self.name


class FacultyInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dean = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
class ExchangeProgram(models.Model):
    name = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    languages = models.CharField(max_length=200)
    places = models.PositiveIntegerField(default=0)
    deadline = models.DateField()
    description = models.TextField()


    def __str__(self):
        return self.name
    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()
