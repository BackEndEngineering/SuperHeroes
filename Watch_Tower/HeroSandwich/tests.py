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
        info = Character.objects.all()
        self.assertEquals(3, len(info))

    def testCharacterView(self):
        client = Client()
        info = Character.objects.order_by("name")[0]
        url = reverse('characters:view', args=[info.id])
        resp = client.get(url)
        self.assertContains(resp, info.name)

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
        info = Description.objects.all()
        self.assertEquals(3, len(info))


    def testDescriptionView(self):
        client = Client()
        info = Description.objects.order_by("real_name")[0]
        url = reverse('characters:description', args=[info.id])
        resp = client.get(url)
        self.assertContains(resp, info.real_name)
