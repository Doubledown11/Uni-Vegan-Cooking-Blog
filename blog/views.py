from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from .forms import CommentForm, SearchForm

from django.core.cache import cache
from django.core.mail import EmailMessage

# View to lead to Page for responsive design 
def responsive(request):
    return render(request, 'blog/base_responsive.html')


def blog_category_responsive(request, category): 
    posts = Post.objects.filter(
        categories_name_contains=category
    ).order_by("-created_on")
    context = {
        "category" : category, 
        "posts" : posts,
    }
    return render(request, "blog/category.html", context)



def blog_detail_responsive(request, pk):
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


def blog_index_reponsive(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/responsive.html", context)




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
    """
    TODO
    """

    return render(request, "blog/base.html")




def blog_index(request):
    """
    Renders the base template, and also IDs if the dark mode is set in the cache.
    """

    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }


    # Check cache on load and refresh to see
    dark = cache.get('cache_key')
    print('dark cache data get', dark, '\n\n')

    if dark == None:     
        return render(request, "blog/base.html", context)

    print('dark while dark mode set in blog_idx', dark)
    print('\n\n\n')

    if dark == 1:  
        context['cache_key'] = True
    
    return render(request, "blog/base.html", context)

    





def login(request):
    """
    Renders the login page
    """
    return render(request, 'blog/sign_in.html')



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




def send_enquiry(request):
    """
    Sends a contact enquiry to me when submitted by the user. 
    """

    if request.method == 'POST':
        to_email = '' #My email: dalice@ualberta.ca 

        message = '' #The information from contact form formatted


        email = EmailMessage('User Contact Enquiry', message=message, to=to_email)
    




def update_cache(request): 
    """
    Updates the dark mode cache when the button is pressed by the user.
    """

    print('\n\n\nupdate_cache function called\n\n\n')

    print('request data?' , request.POST, '\n\n\n')

    if request.method == 'POST':
        dark = cache.get('cache_key')
        print('dark in update_cache', dark)
        print('\n\n\n')

        if dark == None or dark == 0:
            # Turns on the dark mode 
            cache.set('cache_key', 1, timeout=32000) # Cache for 1 hour
            
            dark = cache.get('cache_key')
            print('verify cache values been set', dark)


        elif dark == 1: 
            # Turns off the dark mode
            cache.set('cache_key', 0, timeout=32000) # Cache for 1 hour
            

        

