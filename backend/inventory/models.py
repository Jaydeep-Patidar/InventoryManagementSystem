from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self): return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=150)
    contact_info = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self): return self.name

class Customer(models.Model):
    name = models.CharField(max_length=150)
    contact_info = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField(default=5)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    def __str__(self): return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [('pending','Pending'), ('received','Received'), ('cancelled','Cancelled')]
    order_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    def __str__(self): return f"PO-{self.order_number}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return f"{self.product.name} ({self.quantity})"

class SalesOrder(models.Model):
    PAYMENT_STATUS = [('paid','Paid'), ('pending','Pending')]
    order_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    def __str__(self): return f"SO-{self.order_number}"

class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return f"{self.product.name} ({self.quantity})"

class StockTransaction(models.Model):
    TRANSACTION_TYPE = [('purchase','Purchase'), ('sale','Sale'), ('return','Return'), ('adjustment','Adjustment')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    remarks = models.TextField(blank=True, null=True)
    def __str__(self): return f"{self.transaction_type} - {self.product.name} ({self.quantity})"

class StockAdjustment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    adjustment_quantity = models.IntegerField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self): return f"Adjustment - {self.product.name} ({self.adjustment_quantity})"

class ReturnRecord(models.Model):
    RETURN_TYPE = [('purchase','Purchase Return'), ('sale','Sales Return')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    return_type = models.CharField(max_length=20, choices=RETURN_TYPE)
    quantity = models.PositiveIntegerField()
    reason = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self): return f"{self.return_type} - {self.product.name} ({self.quantity})"
