from django.urls import path
from App_Shop import views
app_name = 'App_Shop'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('product_detail/<pk>/', views.Product_detail.as_view(), name='product_detail'),

]
