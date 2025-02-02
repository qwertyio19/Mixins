from rest_framework.routers import DefaultRouter
from apps.main.views import ProductAPI, CategoryAPI, CarAPI, CategoryCarAPI



router = DefaultRouter()

router.register('product', ProductAPI, basename='api_products')
router.register('category', CategoryAPI, basename='api_category')
router.register("car", CarAPI, basename="api_car")
router.register("category_car", CategoryCarAPI, basename="api_category_car")

urlpatterns = router.urls