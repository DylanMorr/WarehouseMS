# Generated by Django 4.2 on 2023-04-21 04:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_api", "0003_delete_orders"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("Oid", models.AutoField(primary_key=True, serialize=False)),
                ("Order_Id", models.IntegerField()),
                (
                    "Product_Ids",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "Product_Qtys",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("Buyer_Name", models.CharField(max_length=100)),
                ("Buyer_Address", models.CharField(max_length=150)),
            ],
        ),
    ]
