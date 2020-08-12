from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def review_list(request):
    review_lists = Question.objects.order_by('-pub_date')
    return render(request, 'review/review_list.html', {'review_lists': review_lists})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, qustion_id):
    return HttpResponse("You're voting on question %s." % qustion_id)