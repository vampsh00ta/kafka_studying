from django.urls import path,re_path
from . import views



from django.urls import path,re_path
from . import views

urlpatterns = [
    path('items/<int:id>/', views.GetItems.as_view()),
    path('items/', views.GetItems.as_view()),

    path('addToBasket/', views.AddToBasket.as_view()),
    path('basket/', views.Basket.as_view()),
    path('order/', views.MakeOrder.as_view()),
    path('orders/', views.GetOrders.as_view()),

]