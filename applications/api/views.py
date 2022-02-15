
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import *
from  ..models import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



# class UserView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class= UserSerializer



# class CategoryView(viewsets.ModelViewSet):
#     queryset=Category.objects.all()
#     serializer_class= CategorySeriallizers

# class SubCategoryView(viewsets.ModelViewSet):
#     queryset=SubCategory.objects.all()
#     serializer_class= SubCategorySeriallizers


# class ProductView(viewsets.ModelViewSet):
#     queryset=Product.objects.all()
#     serializer_class= ProductSerialezer

# class OrderView(viewsets.ModelViewSet):
#     queryset=Order.objects.all()
#     serializer_class= OrderSerializers

# class ShippingView(viewsets.ModelViewSet):
#     queryset=ShippingAddress.objects.all()
#     serializer_class= shippingSerializer
    

@api_view(['POST','DELETE','PUT','GET'])
def UserView1(request,pk):
    if request.method == 'GET':
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        user=User.objects.get(id=pk)
        serializer=UserSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        user=User.objects.get(id=pk)
        user.delete()
        return Response('item successfully delete')




def category(request,pk):
    if request.method == 'GET':
        cate=Category.objects.all()
        serializer=CategorySeriallizers(cate,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=CategorySeriallizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        cate=Category.objects.get(id=pk)
        serializer=CategorySeriallizers(instance=cate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        cate=Category.objects.get(id=pk)
        cate.delete()
        return Response('item successfully delete')






def subcategory(request,pk):
    if request.method == 'GET':
        subcat=SubCategory.objects.all()
        serializer=SubCategorySeriallizers(subcat,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=SubCategorySeriallizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        subcat=SubCategory.objects.get(id=pk)
        serializer=SubCategorySeriallizers(instance=subcat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        subcat=SubCategory.objects.get(id=pk)
        subcat.delete()
        return Response('User successfully delete')







    
@api_view(['POST','DELETE','PUT','GET'])
def ProductView(request,pk):
    if request.method == 'GET':
        pro=Product.objects.all()
        serializer=ProductSerialezer(pro,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=ProductSerialezer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        pro=Product.objects.get(id=pk)
        serializer=ProductSerialezer(instance=pro,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        pro=Product.objects.get(id=pk)
        pro.delete()
        return Response('Product successfully delete')



@api_view(['POST','DELETE','PUT','GET'])
def orderitem(request,pk):
    if request.method == 'GET':
        crt=Cart.objects.all()
        serializer=CartSerialezer(crt,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=CartSerialezer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        crt=Cart.objects.get(id=pk)
        serializer=CartSerialezer(instance=crt,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        crt=Cart.objects.get(id=pk)
        crt.delete()
        return Response('orderitem successfully delete')






@api_view(['POST','DELETE','PUT','GET'])
def orderitem(request,pk):
    if request.method == 'GET':
        ordtm=OrderItem.objects.all()
        serializer=OrderitemSerilizer(ordtm,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=OrderitemSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        ordtm=OrderItem.objects.get(id=pk)
        serializer=OrderitemSerilizer(instance=ordtm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        ordtm=OrderItem.objects.get(id=pk)
        ordtm.delete()
        return Response('orderitem successfully delete')







@api_view(['POST','DELETE','PUT','GET'])
def Order(request,pk):
    if request.method == 'GET':
        pro=Order.objects.all()
        serializer=OrderSerializers(pro,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'PUT':
        ord=Order.objects.get(id=pk)
        serializer=OrderSerializers(instance=ord,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        ord=Order.objects.get(id=pk)
        ord.delete()
        return Response('order successfully delete')





@api_view(['POST','DELETE','PUT','GET'])
def Shipping(request,pk):
    if request.method == 'GET':
        ship=ShippingAddress.objects.all()
        serializer=shippingSerializer(ship,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=shippingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data=Cart.objects.filter(pro_quantity__gt=0)
            data.update(pro_quantity=0,cart=False,total=0)
            return Response(serializer.data,'order  successfull')
        return Response(serializer._errors)

    if request.method == 'PUT':
        ship=ShippingAddress.objects.get(id=pk)
        serializer=shippingSerializer(instance=ship,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

    if request.method == 'DELETE':
        ship=ShippingAddress.objects.get(id=pk)
        ship.delete()
        return Response('order successfully delete')