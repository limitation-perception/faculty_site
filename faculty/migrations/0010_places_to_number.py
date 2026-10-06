import re

from django.db import migrations


def forward(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places_count = int(re.search(r"\d+", program.places).group())
        program.save()


def backward(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_count)
        program.save()


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0009_exchangeprogram_places_count"),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
