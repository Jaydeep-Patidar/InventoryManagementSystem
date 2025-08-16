from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Supplier, Customer, Product, PurchaseOrder, SalesOrder
from .serializers import (
    CategorySerializer, SupplierSerializer, CustomerSerializer, ProductSerializer,
    PurchaseOrderSerializer, SalesOrderSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        qs = Product.objects.filter(quantity_in_stock__lte=models.F('reorder_level'))
        return Response(self.get_serializer(qs, many=True).data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by('-order_date')
    serializer_class = PurchaseOrderSerializer

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all().order_by('-order_date')
    serializer_class = SalesOrderSerializer





# DENGER CODE FOR PRODUCTION
# views.py
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin@123"
        )
        return HttpResponse("✅ Superuser 'admin' created successfully with password 'Admin@123'")
    else:
        return HttpResponse("⚠️ Superuser already exists.")
