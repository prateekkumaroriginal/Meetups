from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.IndexView.as_view(), name='index'),
    path("meetups/success", views.RegistrationSuccessView.as_view(), name="registration-success"),
    path('meetups/<slug:meetup_slug>', views.MeetupDetailView.as_view(), name='meetup-details')
]
