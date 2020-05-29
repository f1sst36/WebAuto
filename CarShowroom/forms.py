from django import forms
from django.forms import ModelForm

from .models import Reviews, TestDrive, PurchaseCar, ServiceCar


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'mail', 'text',)


class TestDriveForm(ModelForm):
    class Meta:
        model = TestDrive
        fields = ('name', 'surname', 'mail', 'phone', 'car_model', 'time', 'date')


class PurchaseCarForm(ModelForm):
    class Meta:
        model = PurchaseCar
        fields = ('car_model', 'name', 'surname', 'mail', 'phone')


class ServiceForm(ModelForm):
    class Meta:
        model = ServiceCar
        fields = ('work_type', 'name', 'surname', 'mail', 'phone', 'time', 'date')
