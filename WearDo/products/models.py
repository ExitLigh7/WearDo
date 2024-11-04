from django.db import models


class Product(models.Model):

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    stock = models.PositiveIntegerField(
        default=0,
    )

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name="products",
    )

    image = models.ImageField(
        upload_to='products/',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def is_in_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.name