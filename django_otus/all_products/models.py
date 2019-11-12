from django.db import models


# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = (
        (1, 'Cухие корма'),
        (2, 'Наполнители'),
        (3, 'Консервы'),
        (4, 'Лотки'),
        (5, 'Совки'),
        (6, 'Игрушки'),
        (7, 'Домики'),
        (8, 'Переноски'),
    )
    PETS_TYPES = (
        (1, 'Котик'),
        (2, 'Собака'),
    )
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    description = models.CharField(max_length=150)
    name_of_product = models.CharField(max_length=30)
    price = models.FloatField()
    if_in_stock = models.BooleanField(default=True)
    category_pets = models.IntegerField(choices=PETS_TYPES)
    category_of_product = models.IntegerField(choices=PRODUCT_TYPES)
    stock_date = models.DateField(auto_now_add=True)

    def get_oldest_products(number_of_elements=6):
        query = Product.objects.all().order_by('-stock_date')[:number_of_elements]
        return query

    def __str__(self):
        return self.name_of_product
