from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def publication(request):
    return render(request, 'publication.html', {'title': 'Publication'})

def service(request):
    return render(request, 'service.html')