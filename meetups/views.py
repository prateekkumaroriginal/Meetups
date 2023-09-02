from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Meetup

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
        except Exception as e:
            selected_meetup = None
        return render(request, 'meetups/meetup_detail.html', {
            'meetup': selected_meetup
        })
