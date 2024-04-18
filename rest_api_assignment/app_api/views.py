from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .seralizer import *
from rest_framework.views import APIView



# Create your views here.
class productAPI(APIView):
    def get(self,request):
        prodata = Product.objects.all()
        seralizer = ProductSerializer(prodata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            prodata =  ProductSerializer(data=request.data)
            if not prodata.is_valid():
                return Response({'status':'202','errors':prodata.errors,'message':"something went wrong"})
            prodata.save()
            return Response({"data":prodata.data,"message":"Product inserted"})

    def put(self,request):
        try:
            pdata = Product.objects.get(id=request.data['id'])
            psdata =  ProductSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Product Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Product.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Product Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})  




 # book - author...   


class bookAPI(APIView):
    def get(self,request):
        bookdata = Book.objects.all()
        seralizer = Bookserializer(bookdata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            bookdata =  Bookserializer(data=request.data)
            if not bookdata.is_valid():
                return Response({'status':'202','errors':bookdata.errors,'message':"something went wrong"})
            bookdata.save()
            return Response({"data":bookdata.data,"message":"Product inserted"})

    def put(self,request):
        try:
            bookdata = Book.objects.get(id=request.data['id'])
            bookdata =  Bookserializer(bookdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':bookdata.errors,'message':"something went wrong"})  
            
            bookdata.save()
            return Response({"data":bookdata.data,"message":"Product Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              bookdata = Book.objects.get(id=request.data['id'])
              bookdata.delete()
              return Response({"message":"Product Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})  