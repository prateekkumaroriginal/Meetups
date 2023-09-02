from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.IndexView.as_view())
]
