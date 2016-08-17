from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UrlList
from .forms import PostForm

# Create your views here.
def jobs_list(request):
    posts = UrlList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'jobList/jobs_list.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('jobs_list')
    else:
        form = PostForm()
    return render(request, 'jobList/post_edit.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(UrlList, pk=pk)
    return render(request, 'jobList/post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(UrlList, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'jobList/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(UrlList, pk=pk)
    post.delete()
    return redirect('jobs_list')
