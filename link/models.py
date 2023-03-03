from django.db import models

class Link(models.Model):
    alias = models.CharField(max_length = 30)
    link = models.TextField()
    category = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.alias}"
