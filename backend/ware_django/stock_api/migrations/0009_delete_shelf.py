# Generated by Django 4.2 on 2023-04-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_api", "0008_map_remove_sector_sector_map"),
    ]

    operations = [
        migrations.DeleteModel(name="Shelf",),
    ]
