from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="list"),
    path('updatetask/<str:pk>/',views.updateTask, name="updateTask"),
    path('deletetask/<str:pk>/',views.deleteTask, name="deleteTask")
]