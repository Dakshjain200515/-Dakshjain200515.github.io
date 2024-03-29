# Generated by Django 5.0.1 on 2024-03-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("party_name", models.CharField(max_length=100)),
                ("weight", models.FloatField()),
                ("rate", models.FloatField()),
                ("purity", models.FloatField()),
                ("amount", models.FloatField()),
                ("gst", models.FloatField()),
                ("tds", models.FloatField()),
                ("final_amount", models.FloatField()),
            ],
        ),
    ]
