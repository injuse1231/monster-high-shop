from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def price_formatted(self):
        # Округляем до целого числа
        value = int(round(self.price))
        # Форматируем с разделителями тысяч и заменяем запятую на неразрывный пробел
        return f"{value:,}".replace(",", " ")
