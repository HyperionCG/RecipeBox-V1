from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index)
    #path('admin/', admin.site.urls),
]