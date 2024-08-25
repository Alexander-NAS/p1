from django.urls import path
from carts import views


app_name = "carts"

urlpatterns = [
    path("cart_add/<slug:product_slug>", views.cart_add, name='cart_add'),
    path("cart_increment/<int:cart_id>", views.cart_increment, name='cart_increment'),
    path("cart_decrement/<int:cart_id>", views.cart_decrement, name='cart_decrement'),
    path("cart_remove/<int:cart_id>", views.cart_remove, name='cart_remove'),
    path("user_cart", views.UserCartView.as_view(), name='user_cart'),
]
