from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.my_tasks, name='my_tasks'),
    path('priorities/', views.priorities, name='priorities'),
    path('register/', views.register, name='register'),
    path('api/tasks/add/', views.add_task, name='add_task'),
    path('api/tasks/<int:task_id>/slay/', views.slay_task, name='slay_task'),
    path('api/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('api/tasks/<int:task_id>/', views.get_task, name='get_task'),
]
