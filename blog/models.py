from django.contrib.auth.models import User
from django.contrib.sessions.backends import file
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image

class Post(models.Model):
    maxHeight = 500;
    maxWidth = 500;
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="post_pics")
    likes = models.ManyToManyField(to=User, related_name="likes")
    dislikes = models.ManyToManyField(to=User, related_name="dislikes")
    file = models.FileField(default="default.jpg", upload_to="post_files")
    file_name = models.CharField(max_length=40, default="File")


    @property
    def isImage(self):
        return self.file.name.endswith(".png") or self.file.name.endswith(".jpg") or self.file.name.endswith(".jpeg")
    @property
    def isMusik(self):

        return self.file.name.endswith(".mp3") or self.file.name.endswith(".wav")


    @property
    def countLikes(self):
        return self.likes.count()

    @property
    def countDislikes(self):
        return self.dislikes.count()





    def __str__(self):

        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('blog-home')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)




