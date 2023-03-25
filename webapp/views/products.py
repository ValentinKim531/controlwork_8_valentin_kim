from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Moderators', 'users']).exists()


class ProductCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = "product_create.html"
    model = Product
    form_class = ProductForm
    success_message = "Продукт добавлен"
    groups = ['Moderators']

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(GroupPermissionMixin, SuccessMessageMixin, UpdateView):
    template_name = "product_update.html"
    form_class = ProductForm
    model = Product
    success_message = "Продукт обновлен"
    groups = ['Moderators']

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class ProductDetail(DetailView):
    template_name = "product.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = product.reviews.order_by("-created_at")
        context["reviews"] = reviews
        return context


class ProductDeleteView(GroupPermissionMixin, SuccessMessageMixin, DeleteView):
    template_name = "product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy("index")
    success_message = "Продукт удален"
    groups = ['Moderators']
