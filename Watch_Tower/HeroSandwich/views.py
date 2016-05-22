from django.shortcuts import render, get_object_or_404
from .models import Character, Weapon, SuperHeroPower, Team, ColorEye
#from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    recent_characters = Character.objects.order_by('-publish_date')[:5]
    context = {'recent_characters': recent_characters}
    return render(request, 'HeroSandwich/characters.html', context)

def view_character(request, character_id):

    #try:
    #    character = Character.objects.get(id=character_id)
    character = get_object_or_404(Character, id=character_id)
    #except Character.DoesNotExist:
    #    raise Http404("No such article!")
    context = { 'character': character }
    return render(request, 'HeroSandwich/character_details.html', context)

#def superpowers(request):
#    recent_superpowers = SuperPowers.objects.order_by('-publish_date')[:5]
#    context = {'recent_superpowers': recent_superpowers}
#    return render(request, 'HeroSandwich/superpowers.html', context)

def weapons(request):
    recent_weapons = get_object_or_404(Weapon, id=weapon_id)
    #recent_weapons = Weapon.objectsget(id=hero_id)
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

def teams(request):
    teams = Teams.objects.all()
    context = { 'teams': teams }
    return render(request, 'HeroSandwich/teams.html', context)

def team_details(request, hero_id):
    team = Teams.objects.get(id=hero_id)
    context = { 'team': team }
    return render(request, 'HeroSandwich/team_details.html', context)

def color_eyes(request):
    eyes = ColorEyes.objects.all()
    context = { 'eyes': eyes }
    return render(request, 'HeroSandwich/color_eyes.html', context)

def color_eye_details(request, hero_id):
    eye = ColorEyes.objects.get(id=hero_id)
    context = { 'eye': eye }
    return render(request, 'HeroSandwich/color_eye_details.html', context)
