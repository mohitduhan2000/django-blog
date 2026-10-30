from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from blogs.models import Blog, Category
from .forms import CategoryForm
from .blogforms import BlogForm
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

@login_required(login_url='login')
def dashboard(request):

    # Get blogs created by the logged-in user
    user_blogs = Blog.objects.filter(author=request.user)

    # Count total, published, and draft blogs
    blogs_count = user_blogs.count()
    published_blogs_count = user_blogs.filter(status='Published').count()
    draft_blogs_count = user_blogs.filter(status='Draft').count()

    context = {
        'blogs_count': blogs_count,
        'published_blogs_count': published_blogs_count,
        'draft_blogs_count': draft_blogs_count,
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def category(request):
    return render(request, 'dashboard/category.html')

@login_required(login_url='login')
@permission_required('blogs.add_category', raise_exception=True)
def cat_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'dashboard/cat_add.html', context)

@login_required(login_url='login')
@permission_required('blogs.change_category', raise_exception=True)
def cat_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:   
        form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return render(request, 'dashboard/cat_edit.html', context)

@login_required(login_url='login')
@permission_required('blogs.delete_category', raise_exception=True)
def cat_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category')

def blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.filter(author=request.user)
    context = {
        'blogs' : blogs
    }
    return render(request, 'dashboard/blogs.html', context)

@login_required(login_url='login')
def blog_add(request):
    if request.method == "POST":
       form = BlogForm(request.POST, request.FILES)

       if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        title = form.cleaned_data['title']
        slug = slugify(title)

        unique_slug = slug
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{get_random_string(5)}'

        blog.save()
        return redirect('blogs')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'dashboard/blog_add.html', context)

@login_required(login_url='login')
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = BlogForm(instance=blog)

    context = {'form': form, 'blog': blog}
    return render(request, 'dashboard/blog_edit.html', context)

@login_required(login_url='login')
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    blog.delete()
    return redirect('blogs')
