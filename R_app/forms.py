from django import forms
from .models import Author, Recipe


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

    labels = {
        'FULL_NAME': 'Full Name',
        'EMAIL': 'Email',
        'USERNAME': 'Username',
        'PASSWORD': 'Password'
    }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

    labels = {
        'TITLE': 'Title',
        'INGREDIENTS': 'Ingredients',
        'INSTRUCTIONS': 'Instructions',
        'PICTURE': 'Picture',
        'AUTHOR': 'Author'
    }

