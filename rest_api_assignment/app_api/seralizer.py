from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model=Product
        fields='__all__'
        # depth=1
    
    def to_representation(self, instance):
       self.fields['category'] =  CategorySerializer(read_only=True)
       return super(ProductSerializer, self).to_representation(instance)



    # book-author....  
  
class Authorseralizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields= '__all__'

class Bookserializer(serializers.ModelSerializer):
  
    class Meta:
        model=Book
        fields='__all__'
   
    
    def to_representation(self, instance):
       self.fields['author_name'] =  Authorseralizer(read_only=True)
       return super(Bookserializer, self).to_representation(instance) 