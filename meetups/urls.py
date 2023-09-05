from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:meetup_slug>/success', views.RegistrationSuccessView.as_view(), name='registration-success'),
    path('<slug:meetup_slug>', views.MeetupDetailView.as_view(), name='meetup-details')
]
