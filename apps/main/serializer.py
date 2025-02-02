from rest_framework import serializers
from apps.main.models import Product, Category, Car, CategoryCar



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','description','color','size','price','old_price','quantity')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title','product')


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CategoryCarSerilizers(serializers.ModelSerializer):
    class Meta:
        model = CategoryCar
        fields = "__all__"