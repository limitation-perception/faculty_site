from django.core.management import call_command
from django.db import migrations


def load_data(apps, schema_editor):
    call_command("loaddata", "fsnst")


def delete_data(apps, schema_editor):
    for name in ["Teacher", "Specialty", "Department", "FacultyInfo"]:
        apps.get_model("faculty", name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0002_facultyinfo"),
    ]

    operations = [
        migrations.RunPython(load_data, delete_data),
    ]
