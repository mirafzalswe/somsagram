from django.shortcuts import render
from .models import Postlar
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Home(ListView):
    model = Postlar
    template_name = 'posts/home.html'
    context_object_name = 'postlar'

class PostDetail(DetailView):
    model = Postlar
    template_name = 'posts/post_detail.html'


class CreatePost(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Postlar
    template_name = 'posts/posts_add.html'
    fields = ['image', 'title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated



class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Postlar
    fields = ['title', 'content']
    template_name = 'posts/posts_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDelete(DeleteView):
    model = Postlar
    success_url = reverse_lazy('posts-home')

