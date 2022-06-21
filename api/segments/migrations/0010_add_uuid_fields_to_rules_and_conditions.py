# Generated by Django 3.2.13 on 2022-06-20 16:24

from django.db import migrations, models
import uuid


def set_uuid_for_segment_rule(apps, schema_editor):
    segment_rule_model_class = apps.get_model("segments", "SegmentRule")

    to_update = []

    for rule in segment_rule_model_class.objects.all():
        rule.uuid = str(uuid.uuid4())
        to_update.append(rule)

    segment_rule_model_class.objects.bulk_update(to_update, fields=["uuid"])


def set_uuid_for_segment_condition(apps, schema_editor):
    condition_model_class = apps.get_model("segments", "Condition")

    to_update = []

    for condition in condition_model_class.objects.all():
        condition.uuid = str(uuid.uuid4())
        to_update.append(condition)

    condition_model_class.objects.bulk_update(to_update, fields=["uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0009_add_unique_constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(
            set_uuid_for_segment_condition, reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name='condition',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
        ),
        migrations.AddField(
            model_name='segmentrule',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(
            set_uuid_for_segment_rule, reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name='segmentrule',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
        )
    ]
