from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('product/', views.product, name='page-product'),
    path('product/detail/<int:pk>/', views.detail, name='page-product-detail'),
    path('product/search/', views.search, name='page-product-search'),
]