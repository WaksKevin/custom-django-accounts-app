from django.contrib.auth.models import Group
from django.db import migrations, models

def create_groups(apps, schema_editor):
    Group.objects.get_or_create(name="students")
    Group.objects.get_or_create(name="instructors")
    Group.objects.get_or_create(name="administrators")

def reverse_create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["students", "instructors", "administrators"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_groups, reverse_code=reverse_create_groups),
    ]
