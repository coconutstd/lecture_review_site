from django.shortcuts import render
from .models import Qna
# Create your views here.


def qna_list(request):
    qnas=Qna.object().all().order_by('-q_like')
    return render(request,'qna/qna_list.html',{'qnas':qnas})