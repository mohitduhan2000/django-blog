from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from blogs.models import Blog, Category
from .forms import CategoryForm

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