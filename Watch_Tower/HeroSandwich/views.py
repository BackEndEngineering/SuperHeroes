from django.shortcuts import render
from .models import Character
from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    recent_characters = Character.objects.order_by('-publish_date')[:5]
    context = {'recent_characters': recent_characters}
    return render(request, 'HeroSandwich/characters.html', context)

def view_character(request, character_id):

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        raise Http404("No such article!")
    context = { 'character': character }
    return render(request, 'HeroSandwich/character_details.html', context)
