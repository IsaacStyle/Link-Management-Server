from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name}"
    
class Team(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name}"
    
class Link(models.Model):
    alias = models.CharField(max_length = 30)
    link = models.TextField()
    category = models.CharField(max_length = 30)
    # categoryId = models.OneToOneField(
    #     Category,
    #     on_delete=models.CASCADE,
    #     default=2
    # )
    # team = models.OneToOneField(
    #     Team,
    #     on_delete=models.CASCADE,
    #     default=2
    # )

    def __str__(self):
        return f"{self.alias}"


