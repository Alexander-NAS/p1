from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("Авторизация", views.UserLoginView.as_view(), name='login'),
    # path("Регистрация", views.CatalogView.as_view(), name='registration'),
    # path("Выйти!!!!", views.CatalogView.as_view(), name='logout'),
]
