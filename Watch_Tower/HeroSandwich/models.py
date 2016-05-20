from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    superhero = models.CharField(max_length=256)
    cover_photo = models.OneToOneField('Photo', null=True, related_name='cover_photo')

    real_name = models.CharField(max_length=50)
    First_Appearance = models.CharField(max_length=50)
    height = models.PositiveIntegerField('Height', null=False, default=0)
    weight = models.PositiveIntegerField('Weight', null=False, default=0)
    eye_color = models.CharField(max_length=15)
    hair_color = models.CharField(max_length=15)
    powers_weapons = models.CharField(max_length=256)
    age = models.PositiveIntegerField('Born', null=False, default=0)
    multiuniverse = models.ManyToManyField('Omniverse')

    article_text = models.TextField()

    publish_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    photos = models.ManyToManyField('Photo')

#    ARTicle_CAt (
#    ('LIFESTYLE', 'LIFESTYLE'),
#    ('VARIETY','VARIETY'),
#    ('POLITICS', 'POLITICS')
#    )
#    CATEGORY = MODELS.CHARFIELD(max_length=128, null=False, blank=False, choices=ARTICLE_CAT, default=3)
    # art = Article(category=5)
    # art.category
    authors = models.ManyToManyField(User)
    views = models.PositiveIntegerField(null=False, default=0)
    current = models.BooleanField(null=False, default=True, db_index=True)

    def __str__(self):
        return str(self.id) + ": " + self.superhero

class Comment(models.Model):
    comment_text = models.TextField(max_length=2000, blank=False)
    moderated = models.BooleanField(default=False, null=False)
    likes = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Character, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Photo(models.Model):
    image = models.ImageField()
    photographer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)

class Omniverse(models.Model):
    multiuniverse = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)

class SuperPower(models.Model):
    superpower = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return str(self.id) + ": " + self.superpower

class Weapon(models.Model):
    weapon = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return str(self.id) + ": " + self.weapon

class SuperHero(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_powers(self):
        return self.superheropower_set.all()

    def add_power(self, name, level):
        
        power = Power.objects.get(name=name)
        shp = SuperHeroPower.create(hero=self, power=power, level=level)

        def __str__(self):
            return self.name

class SuperHeroPower(models.Model):
    hero = models.ForeignKey('SuperHero')
    power = models.ForeignKey('Power')
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hero.name + " " + self.power.name + " level: " + str(self.level)

class Power(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    #value = models.IntegerField()
