from django.db import models
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta
from .utils import title_name
from PIL import Image



class Character(models.Model):

    name = models.CharField(max_length=128)
    description = models.OneToOneField('Description', null=True)

    @property
    def cap_name(self):
        return title_name(self.name)

    def __str__(self):
        return self.name

    def get_character(self):
        return self.character_set.all()

    def add_character(self):
        hero = Character.objects.get(name=name)

    def get_powers(self):
        return self.superheropower_set.all()

    def add_power(self, name, level):

        power = Power.objects.get(name=name)
        shp = SuperHeroPower.create(hero=self, power=power, level=level)

    def get_weapons(self):
        return self.superheroweapon_set.all()

    def add_weapon(self, name, description):
        weapon = Weapon.objects.get(name=name)
        hw = SuperHeroWeapon.create(hero=self, weapon=weapon, description=description)

        def __str__(self):
            return str(self.id) + ": " + self.name


class Photo(models.Model):
    image = models.ImageField()
    photographer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)


class SuperPowers(models.Model):
    superpower = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return str(self.id) + ": " + self.superpowers

class SuperHeroWeapon(models.Model):
    hero = models.ForeignKey('Character')
    weapon = models.ForeignKey('Weapon')
    description = models.TextField()

    def __str__(self):
        return self.hero.name + " " + self.weapon.name + " description: " + str(self.description)

class Weapon(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):

        return str(self.id) + ": " + self.name


class SuperHeroPower(models.Model):
    hero = models.ForeignKey('Character')
    power = models.ForeignKey('Power')
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hero.name + " " + self.power.name + " level: " + str(self.level)

class Power(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class ColorEye(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Description(models.Model):
    #cover_photo = models.OneToOneField('Photo', null=True, related_name='cover_photo')
    description = models.TextField()
    image = models.ImageField()
    real_name = models.CharField(max_length=128)
    birth_date = models.DateField(blank=True, null=True)
    height = models.CharField(max_length=175)
    weight = models.CharField(max_length=128)
    powers = models.CharField(max_length=700)
    abilities = models.CharField(max_length=128)
    group_affiliations = models.CharField(max_length=128)
    first_appearance = models.CharField(max_length=128)


    @property
    def age(self):
        return relativedelta(date.today(), self.birth_date)

    def __str__(self):
        return str(self.id) +  " real_name: " + str(self.real_name)
