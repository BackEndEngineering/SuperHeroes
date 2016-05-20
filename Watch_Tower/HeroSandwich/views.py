from django.shortcuts import render
from .models import Character, SuperPower, Weapon, SuperHero, SuperHeroPower
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

def superpowers(request):
    recent_powers = SuperPowers.objects.order_by('-publish_date')[:5]
    context = {'recent_powers': recent_powers}
    return render(request, 'HeroSandwich/superpowers.html', context)

def weapons(request):
    recent_powers = Powers.objects.order_by('-publish_date')[:5]
    context = {'recent_weapons': recent_weapons}
    return render(request, 'HeroSandwich/weapons.html', context)

def heroes_list(request):
    heroes = SuperHero.objects.all()
    context = { 'heroes': heroes }

    return render(request, 'HeroSandwich/heroes.html', context)

def hero_details(request, hero_id):
    hero = SuperHero.objects.get(id=hero_id)
    context = { 'hero': hero }

    return render(request, 'HeroSandwich/hero.html', context)
