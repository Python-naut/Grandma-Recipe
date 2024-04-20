from django.db import models

# Create your models here.


class Author(models.Model):
    FULL_NAME = models.CharField(max_length=40)
    EMAIL = models.EmailField(unique=True)
    USERNAME = models.CharField(max_length=20, unique=True)
    PASSWORD = models.CharField(max_length=20)

    def __str__(self):
        return self.FULL_NAME


class Recipe(models.Model):
    TITLE = models.CharField(max_length=40)
    INGREDIENTS = models.TextField()
    INSTRUCTIONS = models.TextField()
    PICTURE = models.FileField()
    AUTHOR = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    def __str__(self):
        return self.TITLE

