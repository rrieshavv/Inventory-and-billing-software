from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout_user, name="logout_user",),
    path('store', views.store, name="store"),
    path('store/product/<int:pk>', views.store_item, name="store_item"),
    path('store/add', views.add_laptop, name="add_laptop"),
    path('store/sale/<int:pk>', views.sale_laptop, name="sale_laptop"),
]
