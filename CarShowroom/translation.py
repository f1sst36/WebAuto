from modeltranslation.translator import register, TranslationOptions
from .models import Product, Car, Transmission, Drive, Engine, Modeltype, StaticInfo


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('tagline', 'description', 'about_design', 'about_comfort',
              'about_controllability',
              'feature_text1',
              'feature_text2',
              'feature_text3',
              'power',
              'acceleration',
              'max_speed',
              )


@register(Engine)
class EngineTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Drive)
class DriveTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Transmission)
class TransmissionTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Modeltype)
class ModeltypeTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(StaticInfo)
class StaticInfoTranslationOptions(TranslationOptions):
    fields = ('electroCarInfo',
              'discountSection',
              'development',
              'trust',
              'guarantees',
              'address',
              'workTime',
              )
