from django.contrib import admin
from .models import Category, Supplier, Customer, Product, PurchaseOrder, PurchaseOrderItem, SalesOrder, SalesOrderItem, StockTransaction, StockAdjustment, ReturnRecord


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact_info','address','gst_number')
    search_fields = ('name', 'contact_info', 'address', 'gst_number')
    list_display_links = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact_info','address')
    search_fields = ('name','contact_info','address')
    list_display_links = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','sku','description','category','price','cost_price','reorder_level','quantity_in_stock')
    search_fields = ('name', 'sku', 'category')
    list_filter = ('price', 'cost_price' )
    list_display_links = ('name',)

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id','order_number','supplier','order_date','status')

@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','product','purchase_order','quantity','cost_price')
    search_fields = ('product', 'purshase_order')
    list_filter = ('product', 'quantity','purchase_order')
    list_display_links = ('product',)

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','order_number','order_date','payment_status')
    search_fields = ('customer','order_number','order_date')
    list_filter = ('order_number','payment_status','order_date')
    list_display_links = ('customer',)

@admin.register(SalesOrderItem)
class SalesOrederItemAdmin(admin.ModelAdmin):
    list_display = ('id','sales_order','product','quantity','selling_price')
    search_fields = ('sales_order', 'product', 'quantity')
    list_display_links = ('product',)

@admin.register(StockTransaction)
class StokeTransactionAdmin(admin.ModelAdmin):
    list_display = ('id','product','transaction_type','quantity','date','remarks')
    search_fields = ('product', 'transaction_type','date')
    list_filter = ('product','transaction_type','date' )
    list_display_links = ('product',)

@admin.register(StockAdjustment)
class StockAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('id','product','adjustment_quantity','reason','date')
    search_fields = ('product', 'adjustment_qunatity','date')
    list_filter = ('product', 'adjustment_quantity','date')
    list_display_links = ('product',)
                
@admin.register(ReturnRecord)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product','return_type','quantity','reason','date')
    search_fields = ('product','return_type','date')
    list_filter = ('product','return_type','date','quantity')
    list_display_links = ('product',)

