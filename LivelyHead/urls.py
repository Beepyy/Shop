from django.urls import path
from .views import CategoryView,GoodListView,GoodView,main
urlpatterns=[
    path('',main,name='main'),
    path('Shop',CategoryView.as_view(),name='Shop'),
    path('Shop/<str:category>/',GoodListView.as_view(),name='cat_goods'),
    path('Shop/<str:category>/<int:pk>',GoodView.as_view(),name='good'),
    
]