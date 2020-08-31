from django.shortcuts import render, HttpResponse
from .models import Lecture, Book
from django.views import generic

# Create your views here.


def index(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')

class lecture_list(generic.ListView):
    template_name = 'lecture/lecture_list.html';
    context_object_name = 'lectures'

    def get_queryset(self):
        print(Lecture.objects.all())
        return Lecture.objects.all()

# def lecture_list(request):
#     lectures = Lecture.objects.all()
#     return HttpResponse(request, 'lecture/lecture_list.html', {'lectures': lectures})


def book_list(request):
    kind = request.GET.get('book_kind')
    book_kind = Book.objects.filter(book_kind=kind)
    return render(request, 'lecture/book_list.html', {'book_kind': book_kind})


def book_type(request):
    return render(request, 'lecture/book_type.html')


def signup(request):
    return render(request, 'registration/signup.html')
