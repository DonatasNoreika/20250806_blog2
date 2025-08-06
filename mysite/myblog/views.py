from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
