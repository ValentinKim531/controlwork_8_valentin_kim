from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import IntegerChoices


class RatingChoice(IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Review(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_DEFAULT,
        max_length=30,
        default=1,
        related_name="reviews",
        verbose_name="Автор",
    )
    product = models.ForeignKey(
        "webapp.Product",
        related_name="reviews",
        on_delete=models.CASCADE,
        verbose_name="Продукт",
    )
    text = models.TextField(
        max_length=2000, verbose_name="Текст", null=False, blank=False
    )
    rating = models.IntegerField(
        verbose_name="Рейтинг",
        null=False,
        blank=False,
        choices=RatingChoice.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f"{self.author} - {self.product} - {self.text[:25]} - {self.rating}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
