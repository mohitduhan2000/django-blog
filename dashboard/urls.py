from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('category/', views.category, name="category"),
    path('category/add/', views.cat_add, name="cat_add"),
    path('category/edit/<int:category_id>/', views.cat_edit, name="cat_edit"),
    path('category/delete/<int:category_id>/', views.cat_delete, name="cat_delete")
]
