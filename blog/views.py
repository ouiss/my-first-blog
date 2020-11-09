from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):   # we have to get the post variable
    # posts = Post.objects.filter(primary_key=pk)  #Post.objects.get(pk=pk)
    # but does it not handle if pk does not exist in the database
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
