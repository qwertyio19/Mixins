from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.main.models import Product, Category, Car, CategoryCar
from apps.main.serializer import ProductSerializers, CategorySerializers, CarSerializers, CategoryCarSerilizers

class ProductAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
        
class CategoryAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CarAPI(GenericViewSet,
             mixins.ListModelMixin,
             mixins.CreateModelMixin,
             mixins.UpdateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CategoryCarAPI(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = CategoryCar.objects.all()
    serializer_class = CategoryCarSerilizers