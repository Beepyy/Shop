from django.shortcuts import render
from django.views.generic import ListView,DeleteView,View
from .models import *

class AnketiView(ListView):
    model=Person
    template_name='Anketi.html'
    context_object_name='Persons' 

class AnketaView(DeleteView):
    model=Person
    template_name='Anketa.html'
    context_object_name='Person' 

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        print(data)
        skills=Skill.objects.filter(person=data['Person'])
        data['Skills']=skills
        return data