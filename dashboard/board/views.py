from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Post, UserClass
from .forms import PostForm, LoginForm


class AuthUser(FormView):
    form_class = LoginForm
    model = UserClass
    template_name = 'auth_user.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return reverse_lazy('posts')
        else:
            return JsonResponse({'message': 'Неправильный логин или пароль'}, status=401)

class PostsView(ListView):
    model = Post
    paginate_by = 5
    content_type = 'posts'
    template_name = 'posts.html'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'posts_create.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('posts')