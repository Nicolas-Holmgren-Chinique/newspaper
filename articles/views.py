from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# this import will prvent none logined in users from being able to access the create 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_update.html"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        # "author",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)