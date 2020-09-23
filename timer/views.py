from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
# Create your views here.
from .models import Timer

# Create your views here.
class TimerHome(generic.TemplateView):
    template_name = 'timer/timer_home.html'
