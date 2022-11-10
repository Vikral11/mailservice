# Generated by Django 4.1.2 on 2022-11-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="data",
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
                ("email", models.CharField(max_length=400)),
                ("mail", models.CharField(max_length=1000000)),
                ("mail_list", models.CharField(max_length=100000)),
            ],
        ),
    ]