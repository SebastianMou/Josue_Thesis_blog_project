from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.paginator import Paginator

from .models import Post, Category, Comment
from .forms import RegisterForm, CommentForm

# Create your views here.
def categories_base(request):
    return {
        'categories_base': Category.objects.all()[:5],
    }

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_list = Post.objects.filter(category=category)
    context = {
        'category': category,
        'category_list': category_list,
    }
    return render(request, 'category.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'contraseña o nombre de usuario incorrecto')
            return redirect('user_login')
    else:
        pass
    return render(request, 'autho/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este correo electrónico ya está registrado.')
                return redirect('user_register')
            else:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'Te has registrado correctamente.')
                login(request, user)
                return redirect('/')
    else:
        form = RegisterForm() 
    context = {
        'form': form,
    }
    return render(request, 'autho/user_register.html', context)

def home(request):
    posts = Post.objects.all()[:12]
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def all_posts(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 24)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
    }
    return render(request, 'all_post.html', context)

def search(request):
    searched = request.GET.get('searched', '')
    results_list = Post.objects.filter(title__icontains=searched)
    paginator = Paginator(results_list, 1)  # Show 1 post per page.

    page_number = request.GET.get("page")
    results = paginator.get_page(page_number)
    context = {
        'results': results,
        'searched': searched,
    }
    return render(request, 'search.html', context)

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories_with_counts = Category.objects.annotate(post_count=Count('product'))[:10]
    recent_posts = Post.objects.all()[:5]

    comments = post.comments.filter(parent=None)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user  # assuming you have user logged in
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                new_comment.parent = parent_comment
            new_comment.save()
            return redirect('details', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'categories_with_counts': categories_with_counts,
        'recent_posts': recent_posts,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'details.html', context)

