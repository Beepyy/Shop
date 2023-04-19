from unicodedata import category
from django.shortcuts import get_object_or_404, render

from django.views.generic import View,ListView,DetailView
from .models import Good,GoodCategory

def main(request):
    return render(request,'main.html')

class CategoryView(ListView):
    model=GoodCategory
    queryset=GoodCategory.objects.all()
    template_name='Categories.html'



class GoodListView(View):
    def get(self,request,*args,**kwargs):
        category=kwargs['category']
        Goods = Good.objects.filter(category__name=category)
        return render(request,'Goods.html',{'Goods':Goods})



class GoodView(DetailView):
    model=Good
    template_name='Good.html'
    context_object_name='Good'
