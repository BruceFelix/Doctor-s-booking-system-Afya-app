from django.shortcuts import render

# Create your views here.
def base(response):
    return render(response, 'base.html')

def landing(request):
    return render(request, 'landing.html')
