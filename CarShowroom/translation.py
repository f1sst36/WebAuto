from modeltranslation.translator import register, TranslationOptions
from .models import Product, Car


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('tagline',
              'description',
              'about_design',
              'about_comfort',
              'about_controllability',
              'feature_text1',
              'feature_text2',
              'feature_text3',
              'power',
              'model_type',
              'drive',
              'transmission',
              'acceleration',
              'max_speed',
              )
