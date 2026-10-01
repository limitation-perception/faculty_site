from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=150)
    head = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    description =models.CharField(max_length=150)
    head_name = models.CharField(max_length=150)
    head_contact = models.CharField(max_length=150)
    department = models.ForeignKey(
    Department, on_delete=models.CASCADE, related_name="programs"
)

    lessons_list = models.CharField(max_length=150)
    def __str__(self):
            return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    degree =models.CharField(max_length=150)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )
    def __str__(self):
            return self.name
