from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})