from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name='main_page'),
    path("shop", views.ShopView.as_view(), name='shop_page'),
    path("shop/search", views.SearchProductView.as_view(), name="shop_search"),
    path("shop/sort", views.SortProductView.as_view(), name="shop_sort"),
    path("cart", views.CartView.as_view(), name='cart_page'),
    path("product/<slug:slug>", views.ProductView.as_view(), name='product_page'),
    path("review/<slug:slug>", views.AddReview.as_view(), name='add_review'),
    path("test-drive", views.TestDriveView.as_view(), name='test_drive'),
    path("record-on-test-drive", views.RecordTestDrive.as_view(), name='record_on_test_drive'),
    path("record-on-test-drive/success", views.ThxRecordTestDrive.as_view(), name='thx_record_on_test_drive'),
    path("models", views.ModelsView.as_view(), name='models_page'),
    path("json-filter", views.JsonFilterCars.as_view(), name='json_filter_cars'),
    path("car/<slug:slug>", views.CarView.as_view(), name='car_detail_view'),
    path("purchase", views.PurchaseCar.as_view(), name='purchase_form'),
    path("service", views.ServiceView.as_view(), name='service_page'),
    path("service/record", views.ServiceCar.as_view(), name='service_record'),
]