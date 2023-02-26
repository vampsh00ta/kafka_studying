from rest_framework import serializers
from api.models import Items,Orders,Orders_items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class OrdersitemsSerializer(serializers.ModelSerializer):
    item = ItemsSerializer(read_only=True)

    class Meta:
        model = Orders_items
        fields = ( 'quantity','item')
class OrdersSerializer(serializers.ModelSerializer):
    orders_items = OrdersitemsSerializer(read_only=True, many=True)
    class Meta:
        model = Orders
        fields = ('id', 'date','orders_items')

