from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField()
    joinedAt = models.DateTimeField(default=timezone.now)
    follower = models.ManyToManyField(to=User, related_name="follower")

    @property
    def followCount(self):
        return self.follower.count()
    @property
    def allFollows(self):
        return self.follower.all()




    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path)
