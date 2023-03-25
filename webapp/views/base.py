from django.views.generic import RedirectView, ListView

from webapp.models import Product


class IndexView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"
    ordering = ("-created_at",)
    paginate_by = 2
    paginate_orphans = 1


class IndexRedirectView(RedirectView):
    pattern_name = "index"
