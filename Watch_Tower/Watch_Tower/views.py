from django.shortcuts import render

def index(request):
    return render(request, 'HeroSandwich/index.html')
