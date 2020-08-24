from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture,Eval
from django.utils import timezone
#햇갈려서 정리
# Lecture: 모델 클래스, lectures : Lecture 모델 내 object 메소드로 객체 모두 받아온 변수!!
def crud_lecture_list(request):
    lectures= Lecture.objects
    return render(request, 'crud/crud_lecture_list.html', {'lectures':lectures})

def eval_list(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    evals = Eval.objects.filter(lect_id = lect_id).order_by('title')
    # filter(조건필드 = 조건값) : 조건에 맞는 값 반환,
    keys = {
        'lect' : lect,
        'evals' : evals
    }
    return render(request, 'crud/eval_list.html', keys)

def write(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    return render(request, 'crud/write.html', {'lect' : lect})

def create(request):
    if request.method== "POST":
        a_eval = Eval()
        a_eval.lect = Lecture.objects.get(lecture_name=request.POST['lect'])
        a_eval.title=request.POST['title']
        a_eval.pub_date = timezone.datetime.now()
        a_eval.text = request.POST['text']
        a_eval.save()
        return redirect('crud_lecture_list')
    else:
        return render(request, 'crud/write.html')

