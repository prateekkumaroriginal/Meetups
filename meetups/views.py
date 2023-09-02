from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

# Create your views here.


class IndexView(View):
    def get(self, request):
        meetups = [
            {
                'title': 'A first Meetup',
                'location': 'Mumbai',
                'slug': 'a-first-meetup'
            },
            {
                'title': 'Second meetup',
                'location': 'Delhi',
                'slug': 'second-meetup'
            }
        ]
        return render(request, 'meetups/index.html', {
            'meetups': meetups,
            'show_meetups': True
        })


class MeetupDetailView(DetailView):
    def get(self, request, meetup_slug):
        selected_meetup = {
            'title': 'A first Meetup',
            'description': 'This is the first meetup of our group'
        }
        return render(request, 'meetups/meetup_detail.html', {
            'meetup': selected_meetup
        })
