from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import CarGuy
from .forms import CreateNewCarGuy

# Create your views here.

class BaseView(generic.TemplateView):
    template_name = 'main/base.html'


class HomeView(generic.TemplateView):
    template_name = 'main/home.html'


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class AboutView(generic.TemplateView):
    template_name = 'main/about.html'


class UpcomingView(generic.TemplateView):
    template_name = 'main/upcoming.html'


class HighlightsView(generic.TemplateView):
    template_name = 'main/highlights.html'


def rsvp(request):
    if request.method == 'POST':
        form = CreateNewCarGuy(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            car = form.cleaned_data['car']

            if car != '':
                u = CarGuy(first_name=first_name, last_name=last_name, email=email, car=car)
                u.save()

            else:
                u = CarGuy(first_name=first_name, last_name=last_name, email=email)
                u.save()
            
            return HttpResponseRedirect(reverse('main:upcoming',))

        else:
            form = CreateNewCarGuy()
            error_message = '*Enter a valid email address*'
            context ={
            'form':form,
            'error_message':error_message
            }
            return render(request, 'main/rsvp.html', context)

    else:
        form = CreateNewCarGuy()
        context ={
        'form':form
        }
        return render(request, 'main/rsvp.html', context)