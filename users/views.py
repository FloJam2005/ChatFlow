from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import UpdateView

from .forms import UserRegisterForm
from .models import Profile


def _create_profile_if_missing(user: User) -> None:
    profile_exists = Profile.objects.filter(user=user).exists()
    if not profile_exists:
        profile = Profile.objects.create(user=user)
        profile.bio = f"Hallo ich bin {user.username}"
        profile.joinedAt = timezone.now()

        profile.save()





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            _create_profile_if_missing(user)
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_profile(request: HttpRequest, username: str):
    user = User.objects.get(username=username)
    _create_profile_if_missing(user)
    print("im user_profile")
    profile = Profile.objects.get(user__username=username)

    context = {"profile": profile}
    return render(request, template_name="users/profile_page.html", context=context)

def userFollow(request, username):
    profile = User.objects.get(username=username).profile
    user = request.user

    if profile.follower.contains(user):
        profile.follower.remove(user)
    else:
        if profile.user != user:
            profile.follower.add(user)
        else:

            messages.warning(request, "You can't follow yourself")


    return redirect("user-profile-page", username=username)
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "users/profile_update.html"
    fields = ["image", "bio" ]

    def form_valid(self, form):
        return super().form_valid(form)
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    def get_success_url(self):
        return reverse("user-profile-page", args=[self.request.user.username])



