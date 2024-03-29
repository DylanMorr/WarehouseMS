# Generated by Django 4.2 on 2023-04-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departments",
            fields=[
                ("Department_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Department_Name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("Employee_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Employee_Name", models.CharField(max_length=100)),
                ("Department", models.CharField(max_length=100)),
                ("DateOfJoining", models.DateField()),
                ("PhotoFileName", models.CharField(max_length=100)),
            ],
        ),
    ]
