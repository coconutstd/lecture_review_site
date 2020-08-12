from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post_board, Comment
from .forms import PostModelForm, PostForm, CommentModelForm
# Create your views here.

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post_board, pk=pk)
    if request.method =='POST':
        # form 객체 생성
        form = CommentModelForm(request.POST)
        # form valid check
        if form.is_valid():
            # author, text 값이 comment 객체에 저장
            comment = form.save(commit=False)
            # comment 객체에 매칭되는 post id를 저장
            comment.post = post
            # db에 저장
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

#Post 삭제
#@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post_board, pk=pk)
    post.delete()
    return redirect('board_list', )


# post 목록 조회 : 게시일 기준으로 과거에 작성한 글을 필터링하여 정렬하여 글목록 가져오기
def board_list(request):

    # querySet 사용하여 db에서 Post 목록 가져오기
    board_list= Post_board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'board/board_list.html', {'board_list': board_list})