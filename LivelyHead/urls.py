from django.urls import path
from .views import *
urlpatterns=[
    path('',main,name='main'),
    path('Shop',CategoryView.as_view(),name='Shop'),
    path('Shop/<str:category>',GoodListView.as_view(),name='cat_goods'),
    path('Shop/<str:category>/<int:pk>',GoodView.as_view(),name='good'),
    path(r'^$', cart_detail, name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]