from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def sam(request):
    return render(request, 'jobs/sam.html')

def detail(request, job_id):
    return render(request, 'jobs/home.html')
