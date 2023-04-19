from django.db import models




class Post(models.Model):
    #category=models.ForeignKey('PostCategory',on_delete=models.SET_DEFAULT,default=None,null=True,blank=True)
    title=models.CharField(unique=True,max_length=45)
    text=models.TextField(max_length=4000)
    image=models.ImageField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title