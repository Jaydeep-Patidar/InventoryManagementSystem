from rest_framework import serializers
from .models import Category, Supplier, Customer, Product, PurchaseOrder, PurchaseOrderItem, SalesOrder, SalesOrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Product
        fields = ['id','name','sku','description','category','category_name','price','cost_price','reorder_level','quantity_in_stock']

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = PurchaseOrderItem
        fields = ['id','product','product_name','quantity','cost_price']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True)
    supplier_name = serializers.ReadOnlyField(source='supplier.name')
    class Meta:
        model = PurchaseOrder
        fields = ['id','order_number','supplier','supplier_name','order_date','status','items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        po = PurchaseOrder.objects.create(**validated_data)
        for item in items_data:
            PurchaseOrderItem.objects.create(purchase_order=po, **item)
        return po

class SalesOrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = SalesOrderItem
        fields = ['id','product','product_name','quantity','selling_price']

class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True)
    customer_name = serializers.ReadOnlyField(source='customer.name')
    class Meta:
        model = SalesOrder
        fields = ['id','order_number','customer','customer_name','order_date','payment_status','items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        so = SalesOrder.objects.create(**validated_data)
        for item in items_data:
            SalesOrderItem.objects.create(sales_order=so, **item)
        return so
