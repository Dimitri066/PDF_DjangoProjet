"""
URL configuration for PDF_DjangoProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PDF_Django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #chemin classique vers la page admin
    path("", views.renvoie_liste_templates, name="list_templates"),
    #chemin vers la liste des templates (chemin de base)
    path("form/<int:id_template>/", views.remplir_formulaire, name="remplir_formulaire"),
    #chemin dynamique vers le template d'id i ex : http://XXXXXX/form/i/
]
