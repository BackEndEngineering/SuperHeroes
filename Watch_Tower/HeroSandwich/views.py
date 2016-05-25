from django.shortcuts import render, get_object_or_404
from .models import Character, Weapon, SuperHeroPower, Team, ColorEye, Description
#from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    recent_characters = Character.objects.all()
    context = {'recent_characters': recent_characters}
    return render(request, 'HeroSandwich/characters.html', context)

def view_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = { 'character': character }
    return render(request, 'HeroSandwich/character_details.html', context)

def view_description(request, character_id):
    description = get_object_or_404(Description, id=character_id)
    context = { 'description': description }
    return render(request, 'HeroSandwich/description_details.html', context)

def description(request):
    recent_descriptions = Description.objects.all()
    context = {'recent_descriptions': recent_descriptions}
    return render(request, 'HeroSandwich/description.html', context)

def weapons(request):
    recent_weapons = Weapon.objects.all()
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
