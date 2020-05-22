from django.contrib import admin
from .models import User, Product, Reviews
from modeltranslation.admin import TranslationAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'price', 'rating', 'slug']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


admin.site.site_title = "Автосалон"
admin.site.site_header = "Админ панель автосалона"
