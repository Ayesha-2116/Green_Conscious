from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def community_page(request):
    userLoggedIn = True
    if not request.user.is_authenticated:
        userLoggedIn = False
    posts = Post.objects.all()
    return render(request, 'community/community_page.html', {'posts': posts, 'userLoggedIn': userLoggedIn})


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('Login_SignUp:homePage')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community_page')
    else:
        form = PostForm()
    return render(request, 'community/create_post.html', {'form': form})
