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
    id = models.PositiveIntegerField("Идентификатор", unique=True, primary_key=True)
    text = models.TextField("Отзыв")
    name = models.CharField('Имя', max_length=200)
    mail = models.EmailField('Почта')
    date = models.DateTimeField('Дата публикации')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

