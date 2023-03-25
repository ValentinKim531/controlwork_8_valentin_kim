from django.urls import path

from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.products import (
    ProductCreateView,
    ProductDetail,
    ProductUpdateView,
    ProductDeleteView,
)
from webapp.views.review_views import (
    ProductReviewCreateView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "product/", IndexRedirectView.as_view(), name="products_index_redirect"
    ),
    path("product/add", ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path(
        "product/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "product/<int:pk>/confirm_delete/",
        ProductDeleteView.as_view(),
        name="confirm_delete",
    ),
    path(
        "product/<int:pk>/reviews/add/",
        ProductReviewCreateView.as_view(),
        name="product_review_add",
    ),
    path("review/<int:pk>", ReviewDetailView.as_view(), name="review_detail"),
    path(
        "review/<int:pk>/update/",
        ReviewUpdateView.as_view(),
        name="review_update",
    ),
    path(
        "review/<int:pk>/delete/",
        ReviewDeleteView.as_view(),
        name="review_delete",
    ),
    path(
        "review/<int:pk>/delete/",
        ReviewDeleteView.as_view(),
        name="confirm_review_delete",
    ),
]
