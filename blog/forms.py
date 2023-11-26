from django.forms import ModelForm

from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["category", "title", "content", "image1", "image2"]