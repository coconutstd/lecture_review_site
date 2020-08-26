from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from myaccount.models import MyUser
from django.conf import settings
from .models import Post_board, Comment
from .forms import PostForm, CommentModelForm, PostModelForm


# Create your views here.

# comment 승인
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('board_detail', pk=comment.postboard.pk)


# comment 삭제
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    postboard_pk = comment.postboard.pk
    comment.delete()
    return redirect('board_detail', pk=postboard_pk)


# Comment 등록
def add_comment_to_board(request, pk):
    postboard = get_object_or_404(Post_board, pk=pk)
    if request.method == 'POST':
        # form 객체 생성
        form = CommentModelForm(request.POST)
        # form valid check
        if form.is_valid():
            # author, text 값이 comment 객체에 저장
            comment = form.save(commit=False)
            # comment 객체에 매칭되는 post id를 저장
            comment.postboard = postboard
            # db에 저장
            comment.save()
            return redirect('board_detail', pk=postboard.pk)
    else:
        form = CommentModelForm()
    return render(request, 'board/add_comment_to_board.html', {'form': form})


def board_remove(request, pk):
    postboard = get_object_or_404(Post_board, pk=pk)
    postboard.delete()
    return redirect('board_list', )


def board_edit(request, pk):
    postboard = get_object_or_404(Post_board, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=postboard)
        if form.is_valid():
            postboard = form.save(commit=False)
            postboard.author = MyUser.objects.get(nickname=request.user.get_nickname())
            postboard.published_date = timezone.now()
            postboard.save()
            return redirect('board_detail', pk=postboard.pk)
    else:
        form = PostModelForm(instance=postboard)
    return render(request, 'board/board_edit.html', {'form': form})


def board_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            postboard = form.save(commit=False)
            print(request.user.get_nickname())
            postboard.author = MyUser.objects.get(nickname=request.user.get_nickname())
            postboard.published_date = timezone.now()
            postboard.save()
            # postboard = Post_board.objects.create(author=request.user,
            #                            published_date=timezone.now(),
            #                            title=form.cleaned_data['title'],
            #                            text=form.cleaned_data['text'])
            return redirect('board_list')
    else:
        form = PostForm()
    return render(request, 'board/board_edit.html', {'form': form})


# 여기 다시

# post 상세 조회
def board_detail(request, pk):
    board_detail = get_object_or_404(Post_board, pk=pk)
    return render(request, 'board/board_detail.html', {'board_detail': board_detail})


# post 목록 조회 : 게시일 기준으로 과거에 작성한 글을 필터링하여 정렬하여 글목록 가져오기
def board_list(request):
    # querySet 사용하여 db에서 Post 목록 가져오기
    board_list = Post_board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(len(board_list))
    return render(request, 'board/board_list.html', {'board_list': board_list})
