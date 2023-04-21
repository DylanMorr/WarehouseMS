from rest_framework import serializers
from stock_api.models import Stock, Orders, Sector, Shelf, Map

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields=('Sid', 'Stock_Name', 'Supplier', 'Product_Id', 'Price', 'Quantity', 'Location_Sector', 'Location_Shelf', 'PhotoImgName')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=('Oid', 'Order_Id', 'Product_Ids', 'Product_Qtys', 'Price', 'Buyer_Name', 'Buyer_Address')

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sector
        fields=('Sector_ID', 'Sector_Name', 'Sector_Capacity')

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shelf
        fields=('Shelf_ID', 'Shelf_Num', 'Shelf_Capacity')

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model=Map
        fields=('Mid', 'Map_Name')