from django.shortcuts import render, get_object_or_404
from .models import Character, Weapon, SuperHeroPower, Team, ColorEye, Description
from django.template import loader
from .utils import calculate_age, title_name
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def my_first_api_view(request):
     pass # do stuff Here

@login_required
def index(request):
    recent_characters = Character.objects.all()
    context = {'recent_characters': recent_characters}
    return render(request, 'HeroSandwich/characters.html', context)

def view_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = { 'character': character, 'prettyage': calculate_age(character.description.age), 'cap': title_name(character.name)}

    return render(request, 'HeroSandwich/character_details.html', context)
    
@csrf_protect
@permission_required('HeroSandwich.moderate_comment')
def view_description(request, description_id):
    description = get_object_or_404(Description, id=description_id)
    response = FileResponse(open(description.image.url, 'rb'), content_type='image/' + image_type)
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

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_value():
            return HttpResponseRedirect('/articles/')
    form = ContactForm()
    return render(request, 'HeroSandwich/contact.html', {'form':form})

def create_article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            articles = form.save()
            return HttpResponseRedirect
        pass
        form = ArticleForm()
        return render(request, 'HeroSandwich/create_article.html', {'form':form})

@permission_required('HeroSandwich.moderate_comment')
def moderate_description(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        pass
    else:
        pass
