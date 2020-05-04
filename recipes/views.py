from django.shortcuts import render

from recipes.models import Recipes

# Create your views here.
def index(request):
    data = Recipes.objects.all()
    return render(request, 'index.html', {'data': data})