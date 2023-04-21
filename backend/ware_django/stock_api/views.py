from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from stock_api.models import Stock, Orders, Sector, Shelf, Map
from stock_api.serializers import StockSerializer, OrderSerializer, SectorSerializer, ShelfSerializer, MapSerializer

from django.core.files.storage import default_storage
    
@csrf_exempt
def stockApi(request, id=0):
    if request.method=='GET':
        stock = Stock.objects.all()
        stock_serializer = StockSerializer(stock, many=True)
        return JsonResponse(stock_serializer.data, safe=False)
    elif request.method=='POST':
        stock_data = JSONParser().parse(request)
        stock_serializer = StockSerializer(data=stock_data)
        if stock_serializer.is_valid():
            stock_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        stock_data = JSONParser().parse(request)
        stock = Stock.objects.get(Sid = stock_data['Sid'])
        stock_serializer = StockSerializer(stock, data=stock_data)
        if stock_serializer.is_valid():
            stock_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        stock = Stock.objects.get(Sid = id)
        stock.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def orderApi(request, id=0):
    if request.method=='GET':
        orders = Orders.objects.all()
        order_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(order_serializer.data, safe=False)
    elif request.method=='POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        order_data = JSONParser().parse(request)
        order = Orders.objects.get(Oid = order_data['Oid'])
        order_serializer = OrderSerializer(order, data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        order = Orders.objects.get(Oid = id)
        order.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def sectorApi(request, id=0):
    if request.method=='GET':
        sectors = Sector.objects.all()
        sector_serializer = SectorSerializer(sectors, many=True)
        return JsonResponse(sector_serializer.data, safe=False)
    elif request.method=='POST':
        sector_data = JSONParser().parse(request)
        sector_serializer = SectorSerializer(data=sector_data)
        if sector_serializer.is_valid():
            sector_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        sector_data = JSONParser().parse(request)
        sector = Sector.objects.get(Sector_ID = sector_data['Sector_ID'])
        sector_serializer = SectorSerializer(sector, data=sector_data)
        if sector_serializer.is_valid():
            sector_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        sector = Sector.objects.get(Sector_ID = id)
        sector.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def shelfApi(request, id=0):
    if request.method=='GET':
        shelfs = Shelf.objects.all()
        shelf_serializer = ShelfSerializer(shelfs, many=True)
        return JsonResponse(shelf_serializer.data, safe=False)
    elif request.method=='POST':
        shelf_data = JSONParser().parse(request)
        shelf_serializer = ShelfSerializer(data=shelf_data)
        if shelf_serializer.is_valid():
            shelf_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        shelf_data = JSONParser().parse(request)
        shelf = Shelf.objects.get(Shelf_ID = shelf_data['Shelf_ID'])
        shelf_serializer = ShelfSerializer(shelf, data=shelf_data)
        if shelf_serializer.is_valid():
            shelf_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        shelf = Shelf.objects.get(Shelf_ID = id)
        shelf.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def mapApi(request, id=0):
    if request.method=='GET':
        map = Map.objects.all()
        map_serializer = MapSerializer(map, many=True)
        return JsonResponse(map_serializer.data, safe=False)
    elif request.method=='POST':
        map_data = JSONParser().parse(request)
        map_serializer = MapSerializer(data=map_data)
        if map_serializer.is_valid():
            map_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        map_data = JSONParser().parse(request)
        map = Map.objects.get(Mid = map_data['Mid'])
        map_serializer = MapSerializer(map, data=map_data)
        if map_serializer.is_valid():
            map_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        map = Map.objects.get(Mid = id)
        map.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)