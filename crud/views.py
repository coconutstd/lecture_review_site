from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture,Eval
from django.utils import timezone
#햇갈려서 정리

def delete(request, eval_id):
    delete_eval =Eval.objects.get(pk = eval_id)
    delete_eval.delete()
    return redirect('crud_lecture_list')

def update(request, eval_id):
    update_eval = get_object_or_404(Eval, pk = eval_id)

    if request.method == "POST":
        update_eval.title = request.POST['title']
        update_eval.pub_date = timezone.datetime.now()
        update_eval.body = request.POST['text']
        update_eval.save()
        return redirect('eval_detail', eval_id = update_eval.id)
    else:
        return render(request, 'crud/update.html', {'update_eval' : update_eval})


def eval_detail(request, eval_id):
    b_eval = get_object_or_404(Eval, pk=eval_id)
    return render(request, 'crud/eval_detail.html', {'b_eval' : b_eval})

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
        print('a_eval', type(a_eval.id), a_eval.id)

        return redirect('eval_detail', eval_id =a_eval.id)
        # return redirect('crud_lecture_list')
    else:
        return render(request, 'crud/write.html')

# Lecture: 모델 클래스, lectures : Lecture 모델 내 object 메소드로 객체 모두 받아온 변수!!
def crud_lecture_list(request):
    lectures= Lecture.objects
    return render(request, 'crud/crud_lecture_list.html', {'lectures':lectures})

