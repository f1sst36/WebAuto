from django import forms
from django.contrib import admin
from .models import Product, Reviews, TestDrive, Car, CarImages, PurchaseCar, ServiceCar
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'price', 'rating', 'slug']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'date', 'text', 'rating')


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'car_model', 'send_data')


@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ('model', 'line', 'price', 'slug')


@admin.register(CarImages)
class CarImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaseCar)
class PurchaseCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'car_model', 'date')


@admin.register(ServiceCar)
class ServiceCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'work_type', 'date_send')


admin.site.site_title = "Автосалон AUDI"
admin.site.site_header = "Админ панель автосалона"
