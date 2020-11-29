from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<product_id>/', views.add_item, name='add_item'),
    path('edit/<product_id>/', views.edit_bag, name='edit_bag'),
    path('remove/<product_id>/', views.remove_from_bag, name='remove_from_bag'),
]
