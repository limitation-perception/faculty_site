from django.urls import path

from faculty import views

app_name = "main_page"
# CHANGE
app_name = "faculty"

urlpatterns = [
    path("", views.main_page, name="main"),
    path("programs/", views.program_list, name="program_list"),
    path("programs/<int:id>/", views.program_detail, name="program_detail"),
    path("departments/", views.department_list, name="department_list"),
    path("departments/<int:id>/", views.department_detail, name="department_detail"),
]
