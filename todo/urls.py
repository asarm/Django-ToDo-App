from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('edit_task/<str:pk>/', views.edit_task, name='edit_task'),
    path('/<str:pk>/', views.delete, name='delete_task'),
]
