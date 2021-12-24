from django.shortcuts import render
from django.views.generic import ListView
from .admin import Post


# Create your views here.
class HomePagView(ListView):
    model = Post
    template_name='home.html'
    context_object_name="all_post_list"