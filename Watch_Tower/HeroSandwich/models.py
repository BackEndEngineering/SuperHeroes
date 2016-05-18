from django.db import models

class Character(models.Model):
    title = models.CharField(max_length=256)
    article_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.title
