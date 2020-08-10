from django.shortcuts import render
from .models import Lecture
# Create your views here.

def index(request):
    return render(request, 'lecture/base.html')

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture/lecture_list.html', {'lectures': lectures} )