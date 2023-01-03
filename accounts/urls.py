from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('customers/<str:pk>/', views.customer, name='customer'),
    path('products/', views.product, name='products'),
    path('order/', views.create_order, name='create_order'),
    path('order/<str:pk>', views.update_order, name='update_order'),
    path('delete/<str:pk>', views.delete_order, name='delete_order'),
]