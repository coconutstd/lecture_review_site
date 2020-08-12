from django.shortcuts import render
from .models import Lecture,Book
# Create your views here.

def index(request):
    return render(request, 'lecture/base.html')

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture/lecture_list.html', {'lectures': lectures} )

######DB에 추가해놨음 books #######
def book_list(request):
    books=Book.objects.all()
    return render(request,'lecture/book_list.html', {'books':books})

######DB에 추가해놨음 books #######