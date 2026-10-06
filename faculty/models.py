from django.db import models


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
    university = models.CharField(max_length=200)  # назва разом з країною
    languages = models.CharField(max_length=200)
    places = models.CharField(max_length=50)  # поки текст: "2 місця", "до 4"
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university
