from django.db import migrations


def split(text):
    if text.endswith(")"):
        name, country = text[:-1].split("(")
    elif " - " in text:
        name, country = text.rsplit(" - ", 1)
    else:
        name, country = text.rsplit(",", 1)
    return name.strip(), country.strip()


def forward(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.name, program.country = split(program.university)
        program.save()


def backward(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = f"{program.name}, {program.country}"
        program.save()


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0006_exchangeprogram_country_exchangeprogram_name"),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
