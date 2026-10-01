from django.contrib import admin

from faculty.models import Department, Specialty, Teacher, FacultyInfo

admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(Teacher)
admin.site.register(FacultyInfo)
