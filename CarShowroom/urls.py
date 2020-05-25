from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name='main_page'),
    path("shop", views.ShopView.as_view(), name='shop_page'),
    path("shop/search", views.SearchProductView.as_view(), name="shop_search"),
    path("cart", views.CartView.as_view(), name='cart_page'),
    path("product/<slug:slug>", views.ProductView.as_view(), name='product_page'),
    path("review/<slug:slug>", views.AddReview.as_view(), name='add_review'),
    path("test-drive", views.TestDriveView.as_view(), name='test_drive'),
    path("record-on-test-drive", views.RecordTestDrive.as_view(), name='record_on_test_drive'),
    path("record-on-test-drive/success", views.ThxRecordTestDrive.as_view(), name='thx_record_on_test_drive')
]