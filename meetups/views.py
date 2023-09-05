from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        meetups = Meetup.objects.all()
        return render(request, 'meetups/index.html', {
            'meetups': meetups,
            'show_meetups': True
        })


class MeetupDetailView(DetailView):
    def get(self, request, meetup_slug):
        try:
            selected_meetup = Meetup.objects.get(slug=meetup_slug)
            form = RegistrationForm()
            return render(request, 'meetups/meetup_detail.html', {
                'meetup': selected_meetup,
                'form': form
            })
        except Exception as e:
            selected_meetup = None
            return render(request, 'meetups/meetup_detail.html', {
                'meetup': selected_meetup,
            })

    def post(self, request, meetup_slug):
        registration_form = RegistrationForm(request.POST)
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data['email']
            participant, _ = Participant.objects.get_or_create(
                email=user_email)
            selected_meetup.participants.add(participant)
            return redirect('registration-success', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup_detail.html', {
            'meetup': selected_meetup,
            'form': registration_form
        })


class RegistrationSuccessView(DetailView):
    model = Meetup
    slug_url_kwarg = 'meetup_slug'
    template_name = 'meetups/registration_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meetup"] = self.get_object()
        return context
