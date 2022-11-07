from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoView, TodoDeleteView, TodoClearView, TodoUpdateView, TodoChangeView

router = DefaultRouter()

urlpatterns = [
    path('todo/', TodoView.as_view()),
    path('todo/delete/', TodoDeleteView.as_view()),
    path('todo/clear/', TodoClearView.as_view()),
    path('todo/update/', TodoUpdateView.as_view()),
    path('todo/change/', TodoChangeView.as_view())
]