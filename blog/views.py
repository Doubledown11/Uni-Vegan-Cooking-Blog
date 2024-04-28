from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from .forms import CommentForm, SearchForm


# Create your views here.

def contact(request):
    return render(request, "blog/contact.html")


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


def base(request):
    return render(request, "blog/base.html")

# Below view is meant to route us to the home page, but the tutorial labelled 
# home as the blog index.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/base.html", context)


def blog_category(request, category): 
    posts = Post.objects.filter(
        categories_name_contains=category
    ).order_by("-created_on")
    context = {
        "category" : category, 
        "posts" : posts,
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
        "form" : CommentForm(),
    }
    return render(request, "blog/detail.html", context)