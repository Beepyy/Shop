from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Gallery

class PhotosListView(ListView):
    model=Gallery
    template_name='Gallery.html'
    context_object_name='Photos'
