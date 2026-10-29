from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Blog

def posts_by_category(request, category_id):

  # categories = Category.objects.all()   #Create Context processors for common date

  try:
    category = get_object_or_404(Category, id=category_id)
    posts = Blog.objects.filter(status="Published", category_id=category_id)
  except:
    return redirect('home')

  context = {
    'posts' : posts,
    'category' : category,
    # 'categories' : categories
  }
  return render(request, 'blogs/post_by_category.html', context)


