from django import forms
from django.contrib import admin
from .models import Product, Reviews, TestDrive, Car, CarImages, PurchaseCar, ServiceCar, Engine, Transmission, Drive, \
    Modeltype, StaticInfo
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


@admin.register(Engine)
class EngineAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(Drive)
class DriveAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(Transmission)
class TransmissionAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(Modeltype)
class ModeltypeAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(StaticInfo)
class StaticInfoAdmin(TranslationAdmin):
    pass


admin.site.site_title = "Автосалон AUDI"
admin.site.site_header = "Админ панель автосалона"
