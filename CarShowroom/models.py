import datetime

from django.db import models
from pyexpat import model

from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


class StaticInfo(models.Model):
    # Главная страница
    name = models.CharField(max_length=200, default='')
    sliderInfo = RichTextUploadingField()

    expYears = models.PositiveSmallIntegerField('Лет опыта')
    workers = models.PositiveSmallIntegerField('Кол-во работников')
    dovrelnyClients = models.PositiveIntegerField('Кол-во клиентов')

    electroCarPicture = models.ImageField('Картинка электромобиля')
    electroCarInfo = RichTextUploadingField()

    discountSection = RichTextUploadingField()

    development = models.TextField()
    trust = models.TextField()
    guarantees = models.TextField()

    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    workTime = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Глав. страница"
        verbose_name_plural = "Глав. страницы"


class Product(models.Model):
    # Деталь для авто
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField("Цена")
    picture = models.TextField("Изображение")
    rating = models.PositiveSmallIntegerField("Рейтинг", default=0)
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("product_page", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"


class Reviews(models.Model):
    # Отзывы
    text = models.TextField("Отзыв")
    name = models.CharField('Имя', max_length=200)
    mail = models.EmailField('Почта')
    date = models.DateTimeField('Дата публикации', null=True)
    rating = models.PositiveSmallIntegerField('Рейтинг отзыва', default=3)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class TestDrive(models.Model):
    # Записи на тест драйв
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    mail = models.EmailField('Почта')
    phone = models.CharField('Телефон', max_length=100)
    car_model = models.CharField('Модель авто', max_length=100)
    time = models.CharField('Время', max_length=50)
    date = models.DateTimeField('Дата')
    send_data = models.DateTimeField('Дата отправки заявки', default=None)

    def __str__(self):
        return f"{self.name} - {self.car_model}"

    class Meta:
        verbose_name = "Запись на тест драйв"
        verbose_name_plural = "Записи на тест драйв"


class Engine(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"


class Drive(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"


class Transmission(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробки передач"


class Modeltype(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип модели"
        verbose_name_plural = "Типы моделей"


class Car(models.Model):
    model = models.CharField('Модель', max_length=100)
    line = models.CharField('Линейка', max_length=100, default='', blank=True)
    price = models.CharField('Цена', max_length=100)
    poster = models.ImageField('Глав. изображение')
    slug = models.SlugField('slug', max_length=200, default='')

    tagline = models.CharField('Слоган', max_length=200, default='')
    description = models.TextField('Описание', default='')

    about_design = models.TextField('Про дизайн', default='', blank=True)
    about_comfort = models.TextField('Про комфорт', default='', blank=True)
    about_controllability = models.TextField('Про управляемость', default='', blank=True)

    feature_number1 = models.CharField('Число первой особенности', max_length=150, default='')
    feature_text1 = models.CharField('Текст первой особенности', max_length=150, default='')
    feature_number2 = models.CharField('Число второй особенности', max_length=150, default='')
    feature_text2 = models.CharField('Текст второй особенности', max_length=150, default='')
    feature_number3 = models.CharField('Число третей особенности', max_length=150, default='')
    feature_text3 = models.CharField('Текст третей особенности', max_length=150, default='')

    power = models.CharField('Мощность', max_length=100, default='')
    number_of_packages = models.CharField('Количество мест', max_length=100, default='')

    model_type = models.ForeignKey(Modeltype, on_delete=models.CASCADE, verbose_name='Тип модели', default='')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, verbose_name='Двигатель', default='')
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, verbose_name='Привод', default='')
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name='Коробка передач', default='')

    acceleration = models.CharField('Разгон', max_length=100, default='')
    max_speed = models.CharField('Максимальная скорость', max_length=100, default='')

    def get_absolute_url(self):
        return reverse("car_detail_view", kwargs={"slug": self.slug})

    def __str__(self):
        return f"AUDI {self.model} {self.line}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class CarImages(models.Model):
    imageSlider1 = models.ImageField('Картинка для слайдера 1')
    imageSlider2 = models.ImageField('Картинка для слайдера 2')
    imageSlider3 = models.ImageField('Картинка для слайдера 3')

    imageAbout1 = models.ImageField('Дизайн')
    imageAbout2 = models.ImageField('Комфорт')
    imageAbout3 = models.ImageField('Управляемость')

    imageGallery1 = models.ImageField('Картинка для галереи 1')
    imageGallery2 = models.ImageField('Картинка для галереи 2')
    imageGallery3 = models.ImageField('Картинка для галереи 3')
    imageGallery4 = models.ImageField('Картинка для галереи 4')
    imageGallery5 = models.ImageField('Картинка для галереи 5')
    imageGallery6 = models.ImageField('Картинка для галереи 6')

    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', default=0)

    def __str__(self):
        return f"AUDI picture {self.car}"

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


class PurchaseCar(models.Model):
    # Запрос к дилеру

    car_model = models.CharField('Модель авто', max_length=200)
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    mail = models.EmailField('Почта')
    phone = models.CharField('Телефон', max_length=100)
    date = models.DateTimeField('Дата записи', default=datetime.datetime.now())

    def __str__(self):
        return f"{self.car_model} - {self.name} - {self.surname}"

    class Meta:
        verbose_name = "Запрос к дилеру"
        verbose_name_plural = "Запросы к дилеру"


class ServiceCar(models.Model):
    # Заявка на сервис

    work_type = models.CharField('Модель авто', max_length=200)
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    mail = models.EmailField('Почта')
    phone = models.CharField('Телефон', max_length=50)
    time = models.CharField('Время', max_length=50)
    date = models.DateTimeField('Дата записи')
    date_send = models.DateTimeField('Дата отправки заявки', default=datetime.datetime.now())

    def __str__(self):
        return f"{self.work_type} - {self.name} - {self.surname}"

    class Meta:
        verbose_name = "Заявка на сервис"
        verbose_name_plural = "Заявки на сервис"
