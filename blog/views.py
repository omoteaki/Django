# from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import BlogPost, Category
from .forms import BlogPostForm


class IndexView(ListView):
    template_name = "index.html"
    # context_object_name = "orderby_records"
    queryset = BlogPost.objects.order_by("-posted_at")

class BlogDetailView(DetailView):
    template_name = "post.html"
    model = BlogPost

class CategoryView(ListView):
    template_name = "index.html"
    category = True

    def get_queryset(self):
        category_id = self.kwargs["category"]
        categories = BlogPost.objects.filter(
            category = category_id).order_by('-posted_at')
        
        # カテゴリのタイトルを直接渡したかった
        # category_title = Category.objects.get(
        #     id = category_id)
        # return [categories,category_title]
        return categories

    # オーバーライド
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['page_title'] = 'hoge'

        return ctx

class AboutView(TemplateView):
    template_name = "about.html"

class CategoryListView(ListView):
    template_name = "categories.html"
    model = Category


@method_decorator(login_required, name="dispatch")
class CreateBlogView(CreateView):
    form_class = BlogPostForm
    template_name = "post_blog.html"
    success_url = reverse_lazy("blog:post_done")

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = "index.html"