from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post_board, Comment
from .forms import PostModelForm, PostForm, CommentModelForm
# Create your views here.

def board_remove(request, pk):
    postboard = get_object_or_404(Post_board, pk=pk)
    postboard.delete()
    return redirect('board_list', )


def board_edit(request, pk):
    # db에서 해당 pk와 매칭되는 Post 객체를 가져온다.
    postboard = get_object_or_404(Post_board, pk=pk)
    if request.method == 'POST':
        # 수정처리
        form = PostModelForm(request.POST, instance=postboard)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board_detail', pk=postboard.pk)
    else:
        # 수정하기 전에 데이터 읽어옴
        form = PostModelForm(instance=postboard)
    return render(request, 'board/board_edit.html', {'form': form})

def board_new(request):

    if request.method =="POST":
        form =PostForm(request.POST)
        if form.is_valid():
            postboard = form.save(commit = False)
            postboard.author = User.objects.get(username=request.user.username)
            postboard.published_date=timezone.now()
            postboard.save()
            # postboard = Post_board.objects.create(author=request.user,
            #                            published_date=timezone.now(),
            #                            title=form.cleaned_data['title'],
            #                            text=form.cleaned_data['text'])
            return redirect('board_list', pk=postboard.pk)
    else:
        form=PostForm()
    return render(request, 'board/board_edit.html',{'form':form})
# 여기 다시

#post 상세 조회
def board_detail(request, pk):
    board_detail = get_object_or_404(Post_board, pk=pk)
    return render(request, 'board/board_detail.html', {'board_detail':board_detail})



# post 목록 조회 : 게시일 기준으로 과거에 작성한 글을 필터링하여 정렬하여 글목록 가져오기
def board_list(request):
    # querySet 사용하여 db에서 Post 목록 가져오기
    board_list= Post_board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'board/board_list.html', {'board_list': board_list})

