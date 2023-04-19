from django.urls import path
from .views import *
urlpatterns=[
    path('',PostsListView.as_view(),name='Posts'),
    path('/<int:pk>',PostView.as_view(),name='Post')
]