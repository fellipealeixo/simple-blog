from .models import Post
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Post

class DetalhesView(generic.DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['texto', 'autor']

class PostUpdate(UpdateView):
    model = Post
    fields = ['texto', 'autor']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('main:index')
