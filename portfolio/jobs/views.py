from django.shortcuts import render

# Create your views here.
def sam(request):
    return render(request, 'jobs/sam.html')
