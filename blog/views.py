from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from enroll.models import UserProfile
from .forms import BlogPostForm, CommentForm

# Create your views here.


@login_required
def create_blog_post(request):
    # Check if the logged-in user has a related UserProfile
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('home')

    if user_profile.user_type != 'doctor':
        return redirect('patient_posts')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_posts')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})


@login_required
def doctor_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_posts.html', {'posts': posts})


@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('doctor_posts')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_blog_post.html', {'form': form, 'post': post})


@login_required
def patient_posts(request):
    categories = set([category[1] for category in BlogPost.CATEGORY])
    posts_by_category = {}

    for category_display, category_value in BlogPost.CATEGORY:
        posts = BlogPost.objects.filter(
            category=category_value, is_draft=False)
        posts_by_category[category_display] = posts

    return render(request, 'patient_posts.html', {'categories': categories, 'posts_by_category': posts_by_category})


@login_required
def read_blog_post(request, post_id):
    user_profile = UserProfile.objects.get(user=request.user)
    user_type = user_profile.user_type
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('read_blog_post', post_id=post_id)
    else:
        comment_form = CommentForm()

    context = {'post': post, 'user_profile': user_profile,
               'comments': comments, 'comment_form': comment_form}
    return render(request, 'read_blog_post.html', context)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('read_blog_post', post_id=post_id)
