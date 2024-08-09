from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('crud/', views.crud_view, name='crud'),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
