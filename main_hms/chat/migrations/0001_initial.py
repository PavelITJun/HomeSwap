# Generated by Django 4.2 on 2024-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
                "ordering": ["-timestamp"],
            },
        ),
    ]
