from django.shortcuts import render


def posts(request):
    return render(request, 'blog/blog.html')
# Create your views here.
