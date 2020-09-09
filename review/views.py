from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Question, Choice
from django.views import generic
from .forms import QuestionChoiceForm

# Create your views here.
class review_list(generic.ListView):
    template_name = 'review/review_list.html'
    context_object_name = 'review_lists'

    def get_queryset(self):
        return Question.objects.order_by('-created_date')[:5]


class ReviewForm(generic.DetailView):
    model = Question
    context_object_name = 'review'
    template_name = 'review/review_form.html'


class ReviewDetail(generic.DetailView):
    model = Question
    template_name = 'review/review_result.html'

@login_required
def review_new(request):
    if request.method == 'POST':
        form = QuestionChoiceForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = QuestionChoiceForm()
    return render(request, 'review/review_new.html', {'form': form})

@login_required
def review_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'review/review_form.html', \
                      {'question': question,
                       'error_message': "You didn't select a choice."
                       })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('review_detail', args=(question.id,)))
