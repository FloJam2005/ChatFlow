from django.urls import path

from blog import views
from blog.views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView, PostCommentView, CommentView, deleteComment, likePost, LikeRedirectView, dislikePost,
)





urlpatterns = [
    #path('', views.test, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name='post-comment'),
    path("post/<int:pk>/comments/", CommentView.as_view(), name="comments"),
    path("comment/<int:pk>/delete/", deleteComment, name="comment-delete"),
    path("post/<int:pk>/like/", likePost, name="likePost"),
    path("post/<int:pk>/likes/redirect/", LikeRedirectView.as_view(), name="redirect_likes"),
    path("post/<int:pk>/dislike/", dislikePost, name="dislikePost")


]
