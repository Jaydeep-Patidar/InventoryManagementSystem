from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SupplierViewSet, CustomerViewSet, ProductViewSet, PurchaseOrderViewSet, SalesOrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'sales-orders', SalesOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
