from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import UrlList
from .forms import PostForm

# Create your views here.
def jobs_list(request):
    posts = UrlList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'jobList/jobs_list.html', {'posts': posts})

'''def post_new(request):
    form = PostForm()
    return render(request, 'jobList/post_edit.html', {'form': form})
'''

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('jobs_list')
    else:
        form = PostForm()
    return render(request, 'jobList/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(UrlList, pk=pk)
    return render(request, 'jobList/post_detail.html', {'post': post})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('jobList.views:jobs_list')
