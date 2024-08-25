from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from bicycles.models import Products
from carts.models import Cart


def cart_add(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)

        if cart.exists():
            cart.quantity += 1
            cart.save()

        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        return redirect('users:login')

    return redirect(request.META["HTTP_REFERER"])


def cart_decrement(requset, cart_id):

    cart = Cart.objects.get(id=cart_id)

    if cart.quantity == 1:
        cart.delete()
    else:
        cart.quantity -= 1
        cart.save()

    return redirect(requset.META["HTTP_REFERER"])


def cart_increment(requset, cart_id):

    cart = Cart.objects.get(id=cart_id)

    cart.quantity += 1
    cart.save()

    return redirect(requset.META["HTTP_REFERER"])


def cart_remove(requset, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(requset.META["HTTP_REFERER"])


class UserCartView(TemplateView):
    template_name = "carts\cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Корзина'
        if self.request.user.is_authenticated:
            context["carts"] = Cart.objects.filter(user=self.request.user)
        return context
    