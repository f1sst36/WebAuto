from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.views.generic.base import View

from .models import Product


class MainView(View):
    '''Главная страница'''

    def get(self, request):
        return render(request, "index.html", context=None)


'''class ShopView(ListView):
    Страница магазина деталей

    paginate_by = 3
    def get(self, request):
        products = Product.objects.all()
        return render(request, "shop.html", {"products": products})'''


class ShopView(ListView):
    '''Страница магазина деталей'''

    model = Product
    queryset = Product.objects.all()
    template_name = "shop.html"

    paginate_by = 3


class SearchProductView(ListView):
    '''Поиск продуктов'''

    model = Product
    template_name = "shop.html"
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("search_query"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        context['search_query'] = self.request.GET.get("search_query")
        return context


class CartView(View):
    '''Страница корзины'''

    def get(self, request):
        return render(request, "cart.html")


class ProductView(DetailView):
    model = Product
    slug_field = "slug"
    template_name = "detail_product.html"


class TestDriveView(View):
    def get(self, request):
        return render(request, "test_drive.html", context=None)
