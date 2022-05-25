import datetime
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Blog

# Create your views here.

def index(request):
    recent_id = 0
    current_datetime = datetime.datetime.now()
    latest_blogs = Blog.objects.order_by('-posted')[:3]
    for blog in latest_blogs:
      if blog.id > recent_id:
        recent_id = blog.id
    return render(request, 'blog/index.html', {'latest_blogs': latest_blogs, 'current_datetime': current_datetime, 'recent_id': recent_id,})

def archive(request):
    current_datetime = datetime.datetime.now()
    all_blogs = Blog.objects.order_by('-posted')
    return render(request, 'blog/archive.html', {'all_blogs': all_blogs, 'current_datetime': current_datetime,})

def post(request, blog_id):
    current_datetime = datetime.datetime.now()
    try:
        post = Blog.objects.get(pk=blog_id)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'blog/post.html', {'post': post, 'current_datetime': current_datetime,})

def about(request):
    current_datetime = datetime.datetime.now()
    return render(request, 'blog/about.html', {'current_datetime': current_datetime})

def contact(request):
    current_datetime = datetime.datetime.now()
    return render(request, 'blog/contact.html', {'current_datetime': current_datetime})

def teapot(request):
    # return http code 418
    return render(request, 'blog/418.html', status=418)

def handler404(request, exception):
    return render(request, 'blog/404.html', {'exception': exception}, status=404)

#def handler500(request, exception):
#    return render(request, 'blog/500.html', {'exception': exception}, status=500)
