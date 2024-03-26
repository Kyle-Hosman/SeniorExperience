# Generated by Django 5.0.3 on 2024-03-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instance_name", models.CharField(max_length=100)),
                ("host_ip", models.GenericIPAddressField()),
                ("user", models.CharField(max_length=100)),
                ("ssh_key_path", models.CharField(max_length=200)),
                ("python_interpreter", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="InventoryItem",
        ),
    ]
