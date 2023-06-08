from django.urls import path
from .views import TaskListView
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('', TaskListView.as_view(), name='task_list'),
]