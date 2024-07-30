from django.urls import path
from bicycles import views

app_name = "bicycles"

urlpatterns = [
    path("<slug:category_slug>", views.CatalogView.as_view(), name='catalog'),
]
