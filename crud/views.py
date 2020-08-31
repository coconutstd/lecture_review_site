from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Eval
from myaccount.models import MyUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def delete(request, eval_id):
    delete_eval = Eval.objects.get(pk=eval_id)
    delete_eval.delete()
    return redirect('crud_lecture_list')

@login_required
def update(request, eval_id):
    update_eval = get_object_or_404(Eval, pk = eval_id)
    if request.method == "POST":
        update_eval.author = request.user
        update_eval.title = request.POST['title']
        update_eval.updated_date = timezone.datetime.now()
        update_eval.body = request.POST['text']
        update_eval.save()
        return redirect('eval_detail', eval_id=update_eval.id)
    else:
        return render(request, 'crud/update.html', {'update_eval': update_eval})


def eval_detail(request, eval_id):
    b_eval = get_object_or_404(Eval, pk=eval_id)
    return render(request, 'crud/eval_detail.html', {'b_eval': b_eval})


# 15 강의평 등록 버튼 눌렀을때 글쓰기 창, lect_id eval_list ->write.html로 이동할때 전달받은 것
@login_required
def write(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    return render(request, 'crud/write.html', {'lect' : lect})

# 16 입력한 내용 저장할 함수, url 통해 전달받기 때문에 create url 만들어줘야
def create(request):
    if request.method == "POST":
        a_eval = Eval()
        # lect은  Lecture 참조 필드, Lecture모델의 모든 객체에 대하여
        # lecture_name이 POST 방식으로 전달받은 lect인 객체 가져오기
        # write.html의 name=lect인 내용을 a_eval.lect에 담아준다
        a_eval.lect = Lecture.objects.get(lecture_name=request.POST['lect'])
        a_eval.author = request.user
        a_eval.title=request.POST['title']
        a_eval.created_date = timezone.datetime.now()

        a_eval.text = request.POST['text']
        a_eval.save()

        return redirect('eval_detail', eval_id=a_eval.id)
        # return redirect('crud_lecture_list')
    else:
        return render(request, 'crud/write.html')


# 8 강의별 선택하여 강의 평이나 강의 등록 버튼 등등 보여주는 페이지
# lect 강의 정보 갖고 올거니까
# evals 강의평 글도 갖고 올거니까 .filter(조건 필드= 조건 값)
## 조금 더 공부 filter..
def eval_list(request, lect_id):
    lect = get_object_or_404(Lecture, pk=lect_id)
    evals = Eval.objects.filter(lect_id=lect_id).order_by('title')
    # render할때 딕셔너리 인자 여러개니까 key로 묶어서 전달위함
    keys = {
        'lect': lect,
        'evals': evals
    }
    return render(request, 'crud/eval_list.html', keys)


# 2. 강의평가 메인 함수 짜기

# 5. 강의리스트가 crud_lecture_list화면에 나타나게 하기
# Lecture: 모델 클래스, lectures : Lecture 모델 내 object 메소드로 객체 모두 받아온 변수!!
# 모델Lecture import, objects메서드로 객체 불러와 lectures변수에 담기
# render통해 lectures를 딕셔너리 형태의 인자로 템플릿에 넘겨주기
def crud_lecture_list(request):
    lectures = Lecture.objects
    return render(request, 'crud/crud_lecture_list.html', {'lectures': lectures})
