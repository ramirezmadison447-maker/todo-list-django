from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('crear/', views.task_create, name='task_create'),
    path('tarea/<int:pk>/', views.task_detail, name='task_detail'),
    path('tarea/<int:pk>/editar/', views.task_update, name='task_update'),
    path('tarea/<int:pk>/eliminar/', views.task_delete, name='task_delete'),
    path('tarea/<int:pk>/completar/', views.task_toggle_complete, name='task_toggle_complete'),
]
