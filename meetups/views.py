from django.shortcuts import render
from django.views import View

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
