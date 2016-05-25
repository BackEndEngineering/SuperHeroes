from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from HeroSandwich.models import Description, Character

class CharacterTestCase(TestCase):
    def setUp(self):
        Character.objects.create(name="Test #1")
        Character.objects.create(name="Test #2")
        Character.objects.create(name="Test #3")

    def testCharacterFields(self):
        first = Character.objects.create(name="Test #1")
        #first = Description.objects.get(name="Test #1")
        self.assertEquals("Test #1", first.name)

    def testGetCharacter(self):
        arts = Character.objects.all()
        self.assertEquals(3, len(arts))

    def testCharacterView(self):
        client = Client()
        art = Character.objects.order_by("name")[:0]
        url = reverse('HerosSandwich-character', args=[art.name])
        resp = client.get(url)
        self.assertContains(resp, art.name)

class DescriptionTestCase(TestCase):
    def setUp(self):
        Description.objects.create(real_name="Test #1")
        Description.objects.create(weight="Test #2")
        Description.objects.create(powers="Test #3")

    def testDescriptionFields(self):
        first = Description.objects.create(real_name="Test #1")
        #first = Description.objects.get(name="Test #1")
        self.assertEquals("Test #1", first.real_name)

    def testGetDescription(self):
        arts = Description.objects.all()
        self.assertEquals(3, len(arts))


    def testDescriptionView(self):
        client = Client()
        art = Description.objects.order_by("real_name")[0]
        url = reverse('HerosSandwich-description', args=[art.real_name])
        resp = client.get(url)
        self.assertContains(resp, art.real_name)
