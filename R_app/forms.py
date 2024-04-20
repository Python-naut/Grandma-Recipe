from django import forms
from .models import Author, Recipe


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

