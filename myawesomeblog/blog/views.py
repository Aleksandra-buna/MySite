from django.shortcuts import render, get_object_or_404
from .models import Post

def posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})

def specific_id(request, id_page):
    post = get_object_or_404(Post, pk=id_page)
    return render(request, 'blog/id_page.html', {'post': post})
# Create your views here.
