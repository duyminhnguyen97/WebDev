from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome, name='admin-index'),
    path('add-drug/', views.addDrug, name='admin-add-drug'),
    path('logout/', views.logout_view, name='logout'),
    path('add-drug/success/', views.addNewDrug, name='admin-new-drug'),
    path('edit/<int:pk>/', views.editDrug, name='admin-edit-drug'),
    path('edit/<int:pk>/success', views.editDrugSuccess, name='admin-edit-drug-success'),
    path('search/', views.search, name='admin-search'),
    path('edit/<int:pk>/delete', views.deleteDrug, name='admin-delete-drug'),
    path('edit/<int:pk>/delete/success', views.deleteDrugSuccess, name='admin-delete-drug-success')
]