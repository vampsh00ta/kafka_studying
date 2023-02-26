
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from api.models import  Items ,Orders,Orders_items
from django.db.models import F
from api.serializer import ItemsSerializer,OrdersSerializer
from rest_framework import viewsets
import re
import json
from .cart import Cart
import datetime
from rest_framework.response import Response
from django.db.transaction import  atomic
from kafka import KafkaProducer,TopicPartition
from dataclasses import dataclass
import dataclasses


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
class Sender:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=self.json_serializer)
    def json_serializer(self,data):
        return json.dumps(data,cls = EnhancedJSONEncoder).encode('utf-8')
    def send_email(self,data):
        print(self.json_serializer(data))

        self.producer.send("email_sender", data)

    # def partioner(self):
    #     partions = self.producer.partitions_for('email_sender')
    #     for partion in partions:
    #         first_topic_part = TopicPartition('email_sender', partion)
    #         print(first_topic_part.count())


sender = Sender()


@dataclass
class EmailMessage:
    order_id:int
    email:str
    type:str


class GetItems(APIView):
    def get(self,request,id=None):
        print(request.session)
        if id is not None:
            items = ItemsSerializer(Items.objects.get(id=id))
        else:

            items = ItemsSerializer(Items.objects.all(), many=True)
        print(items)
        return Response(items.data)


class AddToBasket(APIView):
    def post(self,request):

        cart = Cart(request)
        data = request.data
        if ('product_id' or 'quantity') not in data:
            return Response(400)
        product = Items.objects.get(id = data['product_id'])
        cart.add(product=product ,quantity=data['quantity'])
        return Response(200)
class Basket(APIView):
    def get(self,request):
        cart = Cart(request)
        basket = cart.getItems()
        return Response(basket)

class MakeOrder(APIView):
    def post(self,request):
        with atomic():
            User = get_user_model()
            cart = Cart(request)


            data = request.data

            basket = cart.getItems()
            if not basket:
                return Response({"response": "empty basket"},status=400)
            order = Orders(date = datetime.datetime.now())
            order.save()
            if ('email' or 'username') not in data:
                return Response(400)
            username =  data['username']
            email = data['email']
            if not self.valid_mail(email):
                return Response({"response": "invalid email"},status = 400)

            user = User.objects.filter(username = username).first()
            finalPrice = 0
            for name in basket.keys():
                item = Items.objects.filter(name=name)
                quantity = basket[name]['quantity']
                finalPrice += quantity*int(basket[name]['price'])
                item.update(quantity=F('quantity') - quantity)
                item = Items.objects.get(name=name)
                bunch = Orders_items.objects.create( quantity = quantity,item = item)
                bunch.save()

                order.orders_items.add(bunch)
            order.save()

            user.orders.add(order)
            cart.deleteSess()
            data = EmailMessage(order_id = order.id,email = email,type = "order")
            sender.send_email(data)
            # sender.partioner()
            print(data)
            return Response({'conslusion':finalPrice})
    def valid_mail(self,email):
        res = re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$',email)
        print(res)
        return bool(res)



class GetOrders(APIView):
    def get(self,request):
        orders = OrdersSerializer(Orders.objects.all(), many=True)
        return Response(orders.data)


# class GetOrders(viewsets.ModelViewSet):
#     serializer_class = ItemsSerializer
#     queryset = Items.objects.all()
