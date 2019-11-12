from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ["name_of_product", "price", "if_in_stock", "stock_date"]

    def description_short(self, obj: Product):
        return f'{obj.description[:30]}...'

    class Meta:
        model = Product
