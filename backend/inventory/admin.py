from django.contrib import admin
from .models import Category, Supplier, Customer, Product, PurchaseOrder, PurchaseOrderItem, SalesOrder, SalesOrderItem, StockTransaction, StockAdjustment, ReturnRecord

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Customer)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','sku','description','category','price','cost_price','reorder_level','quantity_in_stock')
    search_fields = ('name', 'sku', 'category')
    list_filter = ('price', 'cost_price' )
    list_display_links = ('name',)

# admin.site.register(PurchaseOrder)
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id','order_number','supplier','order_date','status')

# admin.site.register(PurchaseOrderItem)
@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','product','purchase_order','quantity','cost_price')
    search_fields = ('product', 'purshase_order')
    list_filter = ('product', 'quantity')

admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(StockTransaction)
admin.site.register(StockAdjustment)
admin.site.register(ReturnRecord)
