from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name='main_page'),
    path("shop", views.ShopView.as_view(), name='shop_page'),
    path("shop/search", views.SearchProductView.as_view(), name="shop_search"),
    path("cart", views.CartView.as_view(), name='cart_page'),
    path("product/<slug:slug>", views.ProductView.as_view(), name='product_page'),
    path("test-drive", views.TestDriveView.as_view(), name='test_drive'),
]