from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order from {self.start_date} to {self.end_date}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_at_rent = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # Duration in days

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.product.name} in order {self.order.id}"


