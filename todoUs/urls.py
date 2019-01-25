from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^todoList/',views.todoList.as_view(),name = 'todo list'),
    url(r'^todoListComplete/',views.todoListComplete.as_view(),name = 'toggle complete'),
        
]