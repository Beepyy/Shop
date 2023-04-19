from django.db import models
from django.urls import reverse
from matplotlib.style import available

#Shop
class GoodCategory(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

class Good(models.Model):
    category=models.ForeignKey('GoodCategory',on_delete=models.SET_DEFAULT,default=None)
    name=models.CharField(max_length=200, db_index=True)
    #image=models.ImageField(null=True)
    slug=models.SlugField(max_length=200, db_index=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    in_stock=models.IntegerField(default=0)

    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


class Order(models.Model):
    first_name = models.CharField(max_length=50,default=None)
    last_name = models.CharField(max_length=50,default=None)
    email = models.EmailField(default=None)
    address = models.CharField(max_length=250,default=None)
    postal_code = models.CharField(max_length=20,default=None)
    city = models.CharField(max_length=100,default=None)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

class Order_story(models.Model):
    pass








