from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about', views.AboutView.as_view(), name="about"),
    path('categories', views.CategoryListView.as_view(), name="categories"),
    path('blog-detail/<int:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog/<int:category>', views.CategoryView.as_view(), name="blog_cat"),
    path('post/', views.CreateBlogView.as_view(), name="post"),
    path('', views.CreateBlogView.as_view(), name="post_done"),
]