from django.db import models
from django.contrib.auth.models import AbstractUser





class Items(models.Model):
    id = models.AutoField("id товара", primary_key=True)
    price = models.IntegerField("цена")
    quantity =   models.IntegerField("кол-во")
    name = models.CharField('название товара',max_length=255)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
class Orders_items(models.Model):

    id = models.AutoField("id подзаказа", primary_key=True)
    quantity = models.IntegerField("кол-во товара в подзаказе")
    item = models.ForeignKey(Items, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return f"{self.id}"
class Orders(models.Model):
    orders_items = models.ManyToManyField(Orders_items)

    id = models.AutoField("id заказа", primary_key=True)
    date = models.DateField('время оформления заказа')
    def __str__(self):
        return f"{self.id}"

class User(AbstractUser):
    orders = models.ManyToManyField(Orders)