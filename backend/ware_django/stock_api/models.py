from django.db import models
from django.contrib.postgres.fields import ArrayField

class Stock(models.Model):
    Sid = models.AutoField(primary_key=True)
    Stock_Name = models.CharField(max_length=100)
    Supplier = models.CharField(max_length=100)
    Product_Id = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.IntegerField()
    Location_Sector = models.CharField(max_length=5)
    Location_Shelf = models.IntegerField()
    PhotoImgName = models.CharField(max_length=100)

class Orders(models.Model):
    Oid = models.AutoField(primary_key=True)
    Order_Id = models.IntegerField()
    Product_Ids = ArrayField(models.IntegerField())
    Product_Qtys = ArrayField(models.IntegerField())
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Buyer_Name = models.CharField(max_length=100)
    Buyer_Address = models.CharField(max_length=150)

class Sector(models.Model):
    Sector_ID = models.AutoField(primary_key=True)
    Sector_Name = models.CharField(max_length=100)
    Sector_Capacity = models.IntegerField()

class Shelf(models.Model):
    Shelf_ID = models.AutoField(primary_key=True)
    Shelf_Num = models.IntegerField()
    Shelf_Capacity = models.IntegerField()

class Map(models.Model):
    Mid = models.AutoField(primary_key=True)
    Map_Name = models.CharField(max_length=100)