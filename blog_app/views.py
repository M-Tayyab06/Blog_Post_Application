from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    print(f"Posts retrieved: {posts.count()}")  # Debugging
    for post in posts:
        print(f"Post: {post.title}, Created: {post.created_at}, Image: {post.image}")  # Debugging
    return render(request, 'blog_app/post_list.html', {'posts': posts, 'form': PostForm()})

def post_create(request):
    if request.method == 'POST':
        print("Form submitted")  # Debugging
        print(f"POST data: {request.POST}")  # Debugging
        print(f"FILES data: {request.FILES}")  # Debugging
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            print(f"Post saved: {post.title}, Image: {post.image}")  # Debugging
            return redirect('post_list')
        else:
            print(f"Form errors: {form.errors}")  # Debugging
            if 'image' in form.errors and len(form.errors) == 1:
                post = Post(
                    title=request.POST.get('title'),
                    content=request.POST.get('content'),
                )
                post.save()
                print(f"Post saved without image: {post.title}")  # Debugging
                return redirect('post_list')
            posts = Post.objects.all().order_by('-created_at')
            return render(request, 'blog_app/post_list.html', {'posts': posts, 'form': form})
    return redirect('post_list')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        print(f"Deleted post with ID: {pk}")  # Debugging
        return redirect('post_list')
    return redirect('post_list')
