from django.http import Http404
from django.shortcuts import get_object_or_404, render

from faculty.models import Department, ExchangeProgram, FacultyInfo, Specialty, Teacher


# Create your views here.
def main_page(request):
    faculty = FacultyInfo.objects.first()
    if faculty is None:
        raise Http404("no faculty info ")
    departments = Department.objects.prefetch_related("programs", "teachers")
    return render(
        request,
        "main_page/main_page.html",
        {
            "faculty": faculty,
            "departments": departments,
            "programs_count": Specialty.objects.count(),
            "teachers_count": Teacher.objects.count(),
        },
    )


def program_list(request):
    programs = Specialty.objects.all()
    return render(
        request,
        "programs/program_list.html",
        {"faculty": FacultyInfo.objects.first(), "programs": programs},
    )


def program_detail(request, id):
    program = get_object_or_404(Specialty, id=id)
    lessons = program.lessons_list.splitlines()
    return render(
        request,
        "programs/program_detail.html",
        {
            "faculty": FacultyInfo.objects.first(),
            "program": program,
            "lessons": lessons,
        },
    )


def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "departments/department_list.html",
        {"faculty": FacultyInfo.objects.first(), "departments": departments},
    )


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(
        request,
        "departments/department_detail.html",
        {"faculty": FacultyInfo.objects.first(), "department": department},
    )


def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    country = request.GET.get("country")
    if country:
        programs = programs.filter(country=country)
    return render(
        request,
        "exchange/exchange_list.html",
        {
            "faculty": FacultyInfo.objects.first(),
            "programs": programs,
            "countries": ExchangeProgram.objects.values_list(
                "country", flat=True
            ).distinct(),
            "current_country": country,
        },
    )
