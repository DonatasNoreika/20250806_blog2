from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

class UserPostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


