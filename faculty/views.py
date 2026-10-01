from django.http import Http404
from django.shortcuts import get_object_or_404, render

from faculty.models import Department, FacultyInfo, Specialty

# Create your views here.
def main_page(request):
    faculty = FacultyInfo.objects.first()
    if faculty is None:
        raise Http404("no faculty info ")
    return render(request, "main_page/main_page.html", {"faculty": faculty})

def program_list(request):
    programs = Specialty.objects.all()
    return render(request, "programs/program_list.html", {"programs": programs})

def program_detail(request, id):
    program = get_object_or_404(Specialty, id=id)
    lessons = program.lessons_list.splitlines()
    return render(
        request,
        "programs/program_detail.html",
        {"program": program, "lessons": lessons},
    )
def department_list(request):
    departments = Department.objects.all()
    return render(
        request, "departments/department_list.html", {"departments": departments}
    )
def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(
        request, "departments/department_detail.html", {"department": department}
    )
