# from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, DetailView

from .models import BlogPost, Category

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
