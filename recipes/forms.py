from django import forms
from recipes.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
        name = forms.CharField(max_length=30)
        bio = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)