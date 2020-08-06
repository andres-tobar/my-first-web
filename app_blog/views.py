from django.shortcuts import render
from app_blog.models import post
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    posts=post.objects.order_by('-id')
    
    paginator= Paginator(posts,3)
    page=request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request, "app_blog/blog.html",{'post':posts})

def blog_post(request,slug):

    
    posts=post.objects.filter(slug=slug)
    
    return render(request,"app_blog/blog_post.html",{'post':posts})