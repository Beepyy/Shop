from unicodedata import category
from django.shortcuts import get_object_or_404, render

from django.views.generic import View,ListView,DetailView
from .models import Good,GoodCategory

def main(request):
    return render(request,'main.html')

class CategoryView(ListView):
    model=GoodCategory
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


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Good, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Good, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def product_detail(request, id, slug):
    product = get_object_or_404(Good,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})