from django.contrib import admin
from .models import Character, SuperPowers, Weapon, SuperHeroPower, SuperHeroWeapon, Power, Team, ColorEye, Description, Photo

admin.site.register(Character)
admin.site.register(Photo)
admin.site.register(SuperHeroPower)
admin.site.register(SuperHeroWeapon)
admin.site.register(Power)
admin.site.register(Weapon)
admin.site.register(Team)
admin.site.register(ColorEye)
admin.site.register(Description)



# Register your models here.
