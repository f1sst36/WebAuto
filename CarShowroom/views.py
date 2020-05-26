import datetime
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ReviewsForm, TestDriveForm
from .models import Product, Car


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
    queryset = Product.objects.order_by("-rating")
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
        context['q'] = f'search_query={self.request.GET.get("search_query")}&'
        context['search_query'] = self.request.GET.get("search_query")
        return context


class SortProductView(ListView):
    #Сортировка продутов

    model = Product
    template_name = "shop.html"
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.order_by(self.request.GET.get("criterion"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['c'] = f'criterion={self.request.GET.get("criterion")}&'
        return context


class CartView(View):
    '''Страница корзины'''

    def get(self, request):
        return render(request, "cart.html")


class ProductView(DetailView):
    model = Product
    slug_field = "slug"
    template_name = "detail_product.html"


class AddReview(View):
    def post(self, request, slug):
        form = ReviewsForm(request.POST)
        prod = Product.objects.get(slug=slug)
        rating = request.POST.get("rating")
        if form.is_valid():
            form = form.save(commit=False)
            form.product = prod
            if rating is not None:
                form.rating = rating
            form.date = datetime.datetime.now()
            form.save()
        return redirect(prod.get_absolute_url())


class TestDriveView(View):
    def get(self, request):
        return render(request, "test_drive.html", context=None)


class RecordTestDrive(View):
    def post(self, request):
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            now = datetime.datetime.now()
            form.send_data = now
            form.save()
            send_mail('AUDI Store запись на тест драйв', f"Здравствуйте, {form.name}."
                                                         f"\nВы были записаны на тест-драйв автомобиля {form.car_model}. "
                                                         f"\nПросим явится вас в наш автосалон {form.date.day} числа ({form.date.month} месяца) в {form.time}."
                                                         f"\nТак же, в ближайщее время с вами свяжется наш сотрудник чтобы обсудить детали.",
                      'audistoreshowroom@gmail.com', [form.mail], fail_silently=False)
            return redirect('thx_record_on_test_drive')
        return redirect('main_page')


class ThxRecordTestDrive(View):
    def get(self, request):
        return render(request, 'ThxRecordTestDrive.html', context=None)


class ModelsView(ListView):
    model = Car
    template_name = 'cars.html'