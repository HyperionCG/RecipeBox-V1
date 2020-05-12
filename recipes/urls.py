from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signupview)
    #path('admin/', admin.site.urls),
]