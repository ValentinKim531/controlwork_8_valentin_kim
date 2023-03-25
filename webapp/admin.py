from django.contrib import admin

from webapp.models import Product, Review


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "description",
        "image",
    )
    list_filter = (
        "id",
        "title",
        "category",
    )
    search_fields = ("title", "category")
    fields = ("title", "category", "description", "image")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "product",
        "text",
        "rating",
    )
    list_filter = ("id", "author", "product", "rating")
    search_fields = ("author", "product", "rating")
    fields = (
        "author",
        "product",
        "text",
        "rating",
    )
    readonly_fields = ("id",)


admin.site.register(Review, ReviewAdmin)
