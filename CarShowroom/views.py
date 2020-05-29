import datetime

from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ReviewsForm, TestDriveForm, PurchaseCarForm, ServiceForm
from .models import Product, Car, CarImages


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
    # Сортировка продутов

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
        cars = Car.objects.all()
        return render(request, "test_drive.html", {'cars': cars})


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
                                                         f"\nПросим явиться вас в наш автосалон {form.date.day} числа в {form.time}."
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


class JsonFilterCars(ListView):
    # Фильтр автомобилей

    template_name = 'cars.html'

    def get_queryset(self):
        queryset = Car.objects.filter(
            model__in=self.request.GET.getlist("model")
        ).distinct().values("model", "line", "price", "poster", "slug")
        if not queryset:
            queryset = Car.objects.all().values("model", "line", "price", "poster", "slug")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"cars": queryset}, safe=False)


class CarView(DetailView):
    # Детальная страница машины

    model = Car
    template_name = 'detail_car.html'
    slug_field = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['img'] = CarImages.objects.filter(car__slug=context['car'].slug).first()
        context['cars'] = Car.objects.all()
        return context


class PurchaseCar(View):
    # Запрос к дилеру

    def post(self, request):
        form = PurchaseCarForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            send_mail('AUDI Store запрос дилеру', f"Был отправлен запрос дилеру, побробная инфа в БД.",
                      'audistoreshowroom@gmail.com', ['f1sst36@gmail.com', 'edemmametov2000@gmail.com'],
                      fail_silently=False)
            form.save()
        return redirect('main_page')


class ServiceView(View):
    def get(self, request):
        return render(request, 'service.html', context=None)


class ServiceCar(View):
    # Заявка на сервис

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            send_mail('AUDI Store запись на сервис', f"Здравствуйте, {form.name} {form.surname}.\nВы были записаны на сервис на {form.date.day} число.",
                      'audistoreshowroom@gmail.com', [form.mail],
                      fail_silently=False)
            form.save()
        return redirect('main_page')
