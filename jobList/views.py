from django.shortcuts import render
from django.utils import timezone
from .models import UrlList

# Create your views here.
def jobs_list(request):
    posts = UrlList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'jobList/jobs_list.html', {'posts': posts})
