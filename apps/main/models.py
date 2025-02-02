from django.db import models

# Create your models here.c;
class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название товара'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Описание'
    )
    color = models.CharField(
        max_length=255,
        verbose_name='Цвет'
    )
    size = models.CharField(
        max_length=255,
        verbose_name='Размер'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    old_price = models.IntegerField(
        verbose_name='Старая цена'
    )
    quantity = models.IntegerField(
        verbose_name='Количество продуктов',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
    verbose_name='Дата создания',
    auto_now_add=True
)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Категория'
    )
    product = models.ForeignKey( Product,
                                on_delete=models.SET_NULL,
                                verbose_name="Продукты",
                                null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Car(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Машина"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
        )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class CategoryCar(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Категория"
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Машины"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"