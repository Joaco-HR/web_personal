from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from blog.models import Post, Comment
from blog.forms import CommentForm

def blog_index(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.all().order_by("-created_on")
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(body__icontains=search_query) |
            Q(categories__name__icontains=search_query)
        ).distinct()
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(body__icontains=search_query) |
            Q(categories__name__icontains=search_query)
        ).distinct()
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)