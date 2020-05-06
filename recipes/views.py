from django.shortcuts import render

from recipes.models import Author, Recipe

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipespage.html', {'data': data})

def author(request, id):
    namedata = Author.objects.get(id=id)
    data = Recipe.objects.filter(author=namedata)
    return render(request, 'authorpage.html',
                                        {'namedata': namedata, 'data': data})
