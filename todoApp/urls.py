from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTask', views.addTask, name='addTask'),
    path('tasks', views.tasks, name='tasks'),
    path('delete/<int:id>',views.delete_task, name='delete'),
    path('tasks/update/<int:id>',views.update_task, name='update'),
]
