from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Question

# Create your views here.
def review_list(request):
    review_lists = Question.objects.order_by('-pub_date')
    return render(request, 'review/review_list.html', {'review_lists': review_lists})

def review_detail(request, question_id):
    review = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'review/review_detail.html', {'review': review})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, qustion_id):
    return HttpResponse("You're voting on question %s." % qustion_id)