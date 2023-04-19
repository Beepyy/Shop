from django.shortcuts import render
from django.views.generic import ListView,View,DetailView
from .models import *


class PostsListView(ListView):
    model=Post
    template_name='Posts.html'
    context_object_name='Posts'


class PostView(DetailView):
    model=Post
    template_name='Post.html'
    context_object_name='Post'