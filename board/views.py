from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post_board, Comment
from .forms import PostModelForm, PostForm, CommentModelForm
# Create your views here.



#post 상세 조회
def board_detail(request, pk):
    postboard = get_object_or_404(Post_board, pk=pk)
    return render(request, 'board/board_detail.html', {'postboard':postboard})



# post 목록 조회 : 게시일 기준으로 과거에 작성한 글을 필터링하여 정렬하여 글목록 가져오기
def board_list(request):
    # querySet 사용하여 db에서 Post 목록 가져오기
    board_list= Post_board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'board/board_list.html', {'board_list': board_list})

