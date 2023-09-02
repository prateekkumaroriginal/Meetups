from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.IndexView.as_view(), name='index'),
    path('meetups/<slug:meetup_slug>', views.MeetupDetailView.as_view(), name='meetup-details')
]
