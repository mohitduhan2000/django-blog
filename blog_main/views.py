from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogs.models import Category, Blog

def home(request):
  # categories = Category.objects.all() #Context processor
  featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
  posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-created_at')
  context = {
    # 'categories' : categories,
    'featured_posts' : featured_posts,
    'posts' : posts
  }
  return render(request, 'home.html', context)

def post_details(request, slug):
  # post = Blog.objects.filter(slug=slug)
  try:
    post = get_object_or_404(Blog, slug=slug, status="Published")
  except:
    return render(request, '404.html')

  context = {
    'post' : post
  }
  return render(request, 'post_details.html', context)