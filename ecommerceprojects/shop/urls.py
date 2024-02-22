from django.urls import path

from . import views

urlpatterns = [
    path('',views.allproducts,name='allproducts'),
    path('<slug:slug_cat>/', views.allproducts,name='product_by_category'),
    path('<slug:slug_cat>/<slug_prod>/', views.cat_prod,name='product_details'),

]