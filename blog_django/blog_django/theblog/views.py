from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.db.models import Q


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get(
            'q') is not None else ''
        object_list = Post.objects.filter(
            Q(title__icontains=q) | Q(body__icontains=q))
        return object_list


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = PostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = "/"
