from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.PostListView.as_view(), name='posts'),
    path("userposts/", views.UserPostListView.as_view(), name='userposts'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
