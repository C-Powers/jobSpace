from django.shortcuts import render

# Create your views here.
def jobs_list(request):
    return render(request, 'jobList/jobs_list.html', {})
