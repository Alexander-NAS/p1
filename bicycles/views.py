from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from bicycles.models import Products, Categories


class CatalogView(ListView):
    model = Products
    template_name = "bicycles/catalog.html"
    context_object_name = 'goods'
    paginate_by = 3
    slug_url_kwarg = "category_slug"

    def get_queryset(self):

        category_slug = self.kwargs.get(self.slug_url_kwarg)
        if category_slug == 'all':
            goods = super().get_queryset()
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Каталог'
        context["categories"] = Categories.objects.all()
        return context
      