from django.urls import path
from . import views

urlpatterns = [
    path('review', views.review_list.as_view(), name='review_list'),
    path('review/new/', views.review_new, name='review_new'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('review/<int:pk>/form/', views.ReviewForm.as_view(), name='review_form'),
    # path('review/<int:pk>/results/', views.review_result.as_view(), name='review_result'),
    path('review/<int:question_id>/vote/', views.review_vote, name='review_vote'),
    path('review/like/', views.review_like, name='review_like'),
]
