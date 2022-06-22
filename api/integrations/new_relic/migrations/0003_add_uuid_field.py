# Generated by Django 3.2.13 on 2022-06-22 15:10

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("new_relic", "0002_auto_20210325_1414"),
    ]

    operations = [
        migrations.AddField(
            model_name="newrelicconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("new_relic", "newrelicconfiguration"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="newrelicconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
