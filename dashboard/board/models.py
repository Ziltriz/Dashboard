from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django_quill.fields import QuillField


class UserClass(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username', 'password']

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    rating= models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def like(self):
        self.rating += 1
        self.save()


class Respond(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = QuillField()

    def __str__(self):
        return f'Отклик к посту {self.post.title}'

class OneTimeCode(models.Model):
    code = models.CharField(max_length=8)
