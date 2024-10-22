from .models import Post, UserClass, Respond
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',  'type',  'content', 'author', 'rating']

class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ['text', 'author', 'post']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserClass
        fields = ["email",
                  "password"]

class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(name='Логин',widget=forms.TextInput)
    password = forms.CharField(name='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(name='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = UserClass
        fields = ["email","username","password"]