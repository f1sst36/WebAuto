from django.db import models
from pyexpat import model

from django.urls import reverse


class User(models.Model):
    # Человек, совершивший заказ
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    middle_name = models.CharField('Отчество', max_length=200)
    mail = models.EmailField('Почта')
    phone = models.CharField('Номер телефона', max_length=100)
    address = models.CharField('Адрес', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Product(models.Model):
    # Деталь для авто
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField("Цена")
    picture = models.ImageField("Изображение")
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
    model_type = models.CharField('Тип модели', max_length=100, default='')
    number_of_packages = models.CharField('Количество мест', max_length=100, default='')
    engine = models.CharField('Двигатель', max_length=100, default='')
    drive = models.CharField('Привод', max_length=100, default='')
    transmission = models.CharField('Коробка передач', max_length=100, default='')
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
    imageSlider1 = models.ImageField('Картинка для слайдера 1', default='')
    imageSlider2 = models.ImageField('Картинка для слайдера 2', default='')
    imageSlider3 = models.ImageField('Картинка для слайдера 3', default='')

    imageAbout1 = models.ImageField('Дизайн', default='')
    imageAbout2 = models.ImageField('Комфорт', default='')
    imageAbout3 = models.ImageField('Управляемость', default='')

    imageGallery1 = models.ImageField('Картинка для галереи 1', default='')
    imageGallery2 = models.ImageField('Картинка для галереи 2', default='')
    imageGallery3 = models.ImageField('Картинка для галереи 3', default='')
    imageGallery4 = models.ImageField('Картинка для галереи 4', default='')
    imageGallery5 = models.ImageField('Картинка для галереи 5', default='')
    imageGallery6 = models.ImageField('Картинка для галереи 6', default='')

    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', default=0)

    def __str__(self):
        return f"AUDI picture {self.car}"

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
