from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar, name='calendar'),
    path('wellness/', views.wellness_view, name='wellness'),
]
