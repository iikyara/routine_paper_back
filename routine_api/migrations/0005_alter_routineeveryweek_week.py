# Generated by Django 4.0.1 on 2022-01-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("routine_api", "0004_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routineeveryweek",
            name="week",
            field=models.IntegerField(
                choices=[
                    (0, "日"),
                    (1, "月"),
                    (2, "火"),
                    (3, "水"),
                    (4, "木"),
                    (5, "金"),
                    (6, "土"),
                ],
                default=0,
            ),
        ),
    ]
