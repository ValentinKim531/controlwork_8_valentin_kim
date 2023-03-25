from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from django.core.validators import MinValueValidator


# Create your models here.

class StatusChoice(TextChoices):
    OTHER = "other", "Разное"
    PHONE = "phones", "Смартфоны"
    LAPTOP = "laptops", "Ноутбуки"


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Название",
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория",
        null=False,
        blank=False,
        choices=StatusChoice.choices,
        default=StatusChoice.OTHER,
    )
    description = models.TextField(
        max_length=2000, null=True, blank=True, verbose_name="Описание"
    )
    image = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Ссылка на изображение",
        default="https://texterra.ru/upload/iblock/17a/zk4qwtfo4ttmm4qrgtkne62ncyc70vyj/anons.webp"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name="удалено", null=False, default=False
    )

    def __str__(self):
        return f"{self.title} - {self.category} - {self.description} - {self.image}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
