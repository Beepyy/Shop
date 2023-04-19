from django.urls import path
from .views import *
urlpatterns=[
    path('',AnketiView.as_view(),name='Anketi'),
    path('/<int:pk>',AnketaView.as_view(),name='Anketa')
]