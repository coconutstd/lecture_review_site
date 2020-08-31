from django.shortcuts import render
from .models import Lecture, Book
from crud.models import Eval


# Create your views here.


def index(request):
    six_books = Book.objects.all()[:6]
    six_evals = Eval.objects.all()[:6]
    return render(request, 'main.html', {'books': six_books, 'evals': six_evals})

def main(request):
    return render(request, 'main.html')

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture/lecture_list.html', {'lectures': lectures})


def book_list(request):
    kind = request.GET.get('book_kind')
    book_kind = Book.objects.filter(book_kind=kind)
    return render(request, 'lecture/book_list.html', {'book_kind': book_kind})


def book_type(request):
    return render(request, 'lecture/book_type.html')


def signup(request):
    return render(request, 'registration/signup.html')
