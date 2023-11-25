from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('blog-detail/<int:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog/<int:category>', views.CategoryView.as_view(), name="blog_cat"),
]