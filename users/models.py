from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # first_name = models.CharField(max_length=150, blank=True, null=True)
    # last_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self) -> str:
        return self.username
