from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductReviewForm
from webapp.models import Product, Review


class ReviewDetailView(DetailView):
    template_name = "review.html"
    model = Review


class ProductReviewCreateView(CreateView):
    model = Review
    template_name = "review_create.html"
    form_class = ProductReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect("product_detail", pk=product.pk)


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "review_update.html"
    form_class = ProductReviewForm
    context_object_name = "review"

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.object.pk})


class ReviewDeleteView(DeleteView):
    template_name = "review_confirm_delete.html"
    model = Review
    success_url = reverse_lazy("index")
