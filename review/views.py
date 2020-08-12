from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.views import generic

# Create your views here.
class review_list(generic.ListView):
    template_name = 'review/review_list.html'
    context_object_name = 'review_lists'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class review_detail(generic.DeleteView):
    model = Question
    context_object_name = 'review'
    template_name = 'review/review_detail.html'

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, qustion_id):
    return HttpResponse("You're voting on question %s." % qustion_id)
