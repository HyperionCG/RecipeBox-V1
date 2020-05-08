from django.shortcuts import render, reverse, HttpResponseRedirect

from recipes.models import Author, Recipe
from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def add_author(request):
    html = "generic_form.html"
    
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    
    form = AddAuthorForm()

    return render(request, html, {"form": form})

def add_recipe(request):
    html = "generic_form.html"
    
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']

            )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = AddRecipeForm()

    return render(request, html, {"form": form})

def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipespage.html', {'data': data})

def author(request, id):
    namedata = Author.objects.get(id=id)
    data = Recipe.objects.filter(author=namedata)
    return render(request, 'authorpage.html',
                                        {'namedata': namedata, 'data': data})
