from django.db import migrations, models
import uuid


def generate_repair_ids(apps, schema_editor):
    Repair = apps.get_model("mobiles", "Repair")

    for repair in Repair.objects.filter(repair_id__isnull=True):
        repair.repair_id = "MSM-" + uuid.uuid4().hex[:8].upper()
        repair.save(update_fields=["repair_id"])


class Migration(migrations.Migration):

    dependencies = [
        ("mobiles", "0005_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="repair",
            name="repair_id",
            field=models.CharField(
                max_length=20,
                unique=True,
                null=True,
                editable=False,
            ),
        ),

        migrations.RunPython(
            generate_repair_ids,
            migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name="repair",
            name="repair_id",
            field=models.CharField(
                max_length=20,
                unique=True,
                editable=False,
            ),
        ),
    ]