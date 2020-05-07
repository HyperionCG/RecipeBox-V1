from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe)
    #path('admin/', admin.site.urls),
]