from django.urls import path

from . import views
from .views import Tasks

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloWorld.as_view()),
    path('tasks',Tasks.as_view())
]