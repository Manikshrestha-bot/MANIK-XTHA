from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm  
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})

def header(request):
    return render(request, 'header.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('content') 
        image = request.FILES.get('image')

        if title and body:
            Post.objects.create(title=title, body=body, image=image)
            return redirect('create_post')
    return render(request, 'create_post.html')

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    return render(request, 'post_details.html', {'post': post, 'comments': comments})

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('content')  
        image = request.FILES.get('image')

        if title and body:
            post.title = title
            post.body = body 
            if image:
                post.image = image
            post.save()
            return redirect('post_details', post_id=post.id)
    return render(request, 'update_post.html', {'post': post})

def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        author = request.POST.get('author')
        body = request.POST.get('body')
        if author and body:
            Comment.objects.create(post=post, author=author, body=body)
        return HttpResponseRedirect(reverse('post_details', args=[post_id]))

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('post_details', post_id=post.id)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user_login.html')


def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login') 
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm()  

    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def contact(request):
    return render(request,'contact.html')

def foot(request):
    return render(request, "footer.html")
