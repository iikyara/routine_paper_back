# Generated by Django 4.0.1 on 2022-01-07 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineEveryDay',
            fields=[
                ('routine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='routine_api.routine')),
            ],
            bases=('routine_api.routine',),
        ),
        migrations.CreateModel(
            name='RoutineEveryWeek',
            fields=[
                ('routine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='routine_api.routine')),
                ('week', models.IntegerField()),
            ],
            bases=('routine_api.routine',),
        ),
        migrations.CreateModel(
            name='RoutineSpecDay',
            fields=[
                ('routine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='routine_api.routine')),
                ('date', models.DateField()),
            ],
            bases=('routine_api.routine',),
        ),
    ]