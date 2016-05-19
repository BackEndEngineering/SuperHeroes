from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    title = models.CharField(max_length=256)
    article_text = models.TextField()
    real_name = models.CharField(max_length=50)
    First_Appearance = models.CharField(max_length=50)
    height = models.PositiveIntegerField('Height', null=False, default=0)
    weight = models.PositiveIntegerField('Weight', null=False, default=0)
    eye_color = models.CharField(max_length=15)
    hair_color = models.CharField(max_length=15)
    powers_weapons = models.CharField(max_length=256)
    age = models.PositiveIntegerField('Born', null=False, default=0)
    multiuniverse = models.ManyToManyField('Omniverse')
    publish_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    photos = models.ManyToManyField('Photo')
    cover_photo = models.OneToOneField('Photo', null=True, related_name='cover_photo')
    authors = models.ManyToManyField(User)
    views = models.PositiveIntegerField(null=False, default=0)
    current = models.BooleanField(null=False, default=True, db_index=True)

    def __str__(self):
        return str(self.id) + ": " + self.title

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
    multiuniverse = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
