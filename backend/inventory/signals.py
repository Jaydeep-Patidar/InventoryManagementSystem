from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrderItem, SalesOrderItem, Product, StockTransaction

@receiver(post_save, sender=PurchaseOrderItem)
def increase_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity_in_stock += instance.quantity
        product.save()
        StockTransaction.objects.create(product=product, transaction_type='purchase', quantity=instance.quantity)

@receiver(post_delete, sender=PurchaseOrderItem)
def decrease_stock_on_purchase_delete(sender, instance, **kwargs):
    product = instance.product
    product.quantity_in_stock = max(0, product.quantity_in_stock - instance.quantity)
    product.save()
    StockTransaction.objects.create(product=product, transaction_type='adjustment', quantity=-instance.quantity, remarks='PO item deleted')

@receiver(post_save, sender=SalesOrderItem)
def decrease_stock_on_sale(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity_in_stock = max(0, product.quantity_in_stock - instance.quantity)
        product.save()
        StockTransaction.objects.create(product=product, transaction_type='sale', quantity=-instance.quantity)

@receiver(post_delete, sender=SalesOrderItem)
def increase_stock_on_sale_delete(sender, instance, **kwargs):
    product = instance.product
    product.quantity_in_stock += instance.quantity
    product.save()
    StockTransaction.objects.create(product=product, transaction_type='adjustment', quantity=instance.quantity, remarks='SO item deleted')
