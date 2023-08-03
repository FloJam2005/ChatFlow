from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, RedirectView
)

from users.forms import UserRegisterForm
from .models import Post, Comment


def home(request):
    context = {
        'posts': Post.objects
        .all()
    }
    return render(request, 'blog/home.html', context)


def search(request):
    template = 'blog/home.html'

    query = request.GET.get('q')

    result = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    context = {'posts': result}
    return render(request, template, context)


def test(request):

    if User.is_active():
        form = UserRegisterForm(request.POST)
        return render(request, "users/register.html", {"form": form})

    return PostListView.as_view()


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', "image", "file", "file_name"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', "image", "file", "file_name"]

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "blog/comment_form.html"
    fields = ["content"]
    success_url = reverse_lazy("blog-home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(id=self.kwargs.get("pk"))
        return context

    def form_valid(self, form, **kwargs):

        form.instance.post_id = self.kwargs.get("pk")
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentView(ListView):
    model = Comment
    template_name = "blog/show_post.html"
    context_object_name = "comments"

    def get_queryset(self):
        #comments = Comment.objects.all()


        #liste = [object.id == self.kwargs.get("pk") for object in comments]
        print(self.kwargs.get("pk"))
        liste = Comment.objects.filter(post_id=self.kwargs.get("pk"))
        print(liste)
        return liste



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommentView, self).get_context_data()
        context["post"] = Post.objects.get(id=self.kwargs.get("pk"))
        return context










def deleteComment(request, pk):
    comment = Comment.objects.get(id= pk)
    post = comment.post

    if request.user == comment.author or request.user == post.author:
        comment.delete(keep_parents=True)
    else:
        pass

    return redirect("comments", pk=post.id)


@login_required
def likePost(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    if post.likes.contains(user):
        post.likes.remove(user)
    else:
        post.likes.add(user)
        post.dislikes.remove(user)
    r = request.META.get('HTTP_REFERER')

    r += f"#{pk}"
    #return redirect("redirect_likes", pk=post.id)
    return redirect(r)

@login_required
def dislikePost(request, pk):
    #p = request.GET.get("p")

    post = Post.objects.get(id=pk)
    user = request.user

    if post.dislikes.contains(user):
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)
        post.likes.remove(user)

    r = request.META.get('HTTP_REFERER')

    r += f"#{pk}"
    #return redirect("redirect_likes", pk=post.id)
    return redirect(r, pk=post.id)




class LikeRedirectView(RedirectView):
    pages = {1: "blog-home",
             2: "user-posts",
             3: "comments"
             }
    def get_redirect_url(self, *args, **kwargs):
        #page = self.pages[self.request.GET.get('p')]

        return reverse("blog-home") + f"#{kwargs.get('pk')}"

def about(request):
    return render(request, 'about.html', {'title': 'About'})

