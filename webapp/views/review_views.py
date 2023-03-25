from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductReviewForm
from webapp.models import Product, Review
from webapp.views.products import GroupPermissionMixin


class ReviewDetailView(DetailView):
    template_name = "review.html"
    model = Review


class ProductReviewCreateView(GroupPermissionMixin, PermissionRequiredMixin, CreateView):
    model = Review
    template_name = "review_create.html"
    form_class = ProductReviewForm
    groups = ['users']

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect("product_detail", pk=product.pk)

    def test_func(self):
        return self.get_object().author == self.request.user or \
            self.request.user.has_perm('add_review')


class ReviewUpdateView(GroupPermissionMixin, PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = "review_update.html"
    form_class = ProductReviewForm
    context_object_name = "review"
    groups = ['Moderators']

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user or \
            self.request.user.has_perm('change_review')


class ReviewDeleteView(GroupPermissionMixin, PermissionRequiredMixin, DeleteView):
    template_name = "review_confirm_delete.html"
    model = Review
    success_url = reverse_lazy("index")
    groups = ['Moderators']

    def test_func(self):
        return self.get_object().author == self.request.user or \
            self.request.user.has_perm('delete_review')
