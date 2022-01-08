from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import blog



# Create your views here.
class BlogView(ListView):
    model = blog
    template_name = 'home.html'
    
    
class BlogDetail(DetailView):
    model = blog
    template_name = 'blog_detail.html'
   

class BlogCreate(CreateView):
    model = blog
    template_name = 'blog_create.html'
    fields = ['title','author','post']
   
   
class BlogUpdate(UpdateView):
    model = blog
    fields = ['title', 'post']
    template_name = 'blog-update.html'
   
   
class BlogDelete(DeleteView):
    model = blog
    template_name = 'blog-delete.html'
    success_url = reverse_lazy('home')