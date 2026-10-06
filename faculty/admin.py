from django.contrib import admin

from faculty.models import Department, ExchangeProgram, FacultyInfo, Specialty, Teacher

admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(Teacher)
admin.site.register(FacultyInfo)
admin.site.register(ExchangeProgram)
