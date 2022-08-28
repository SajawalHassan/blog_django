from ast import Delete
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = '__all__'
