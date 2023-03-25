from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "category",
            "description",
            "image",
        )

        labels = {
            "title": "Название",
            "category": "Категория",
            "description": "Описание",
            "image": "ссылка на изображение",
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Заголоаок должен быть длиннее 2 символов")
        if Product.objects.filter(title=title).exists():
            raise ValidationError("Заголовок с таким именем уже есть")
        return title


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "text",
            "rating",
        )
